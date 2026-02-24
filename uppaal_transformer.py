"""
Transform parsed SysML model to UPPAAL-compatible JSON structure
"""

def transform_to_uppaal(parsed_model):
    """
    Convert parsed SysML model to UPPAAL-compatible JSON
    
    Args:
        parsed_model: Dict with 'package', 'imports', 'actions', 'parts'
    
    Returns:
        Dict with UPPAAL structure (templates, channels, global declarations, etc.)
    """
    if not parsed_model.get('actions'):
        raise ValueError("No actions found in model")
    
    # Assume first action is the main mission
    mission = parsed_model['actions'][0]
    
    # Extract parts (agents)
    parts = mission.get('parts', [])
    nested_actions = mission.get('nested_actions', [])
    flow = mission.get('flow', [])
    
    # Build UPPAAL structure
    uppaal_model = {
        "package": parsed_model.get('package'),
        "model": {
            "name": mission['name'],
            "type": "action"
        }
    }
    
    # 1. Extract data flow and create global variables
    data_flow_info = extract_data_flow(nested_actions, parts)
    uppaal_model["model"]["global_declarations"] = create_global_declarations(data_flow_info, mission)
    
    # 2. Create channels for synchronization
    uppaal_model["model"]["channels"] = create_channels(nested_actions)
    
    # 3. Create templates (Controller + Agents)
    templates = []
    
    # Controller template
    controller = create_controller_template(flow, nested_actions, data_flow_info)
    templates.append(controller)
    
    # Agent templates
    for part in parts:
        agent_template = create_agent_template(part, nested_actions, data_flow_info)
        templates.append(agent_template)
    
    uppaal_model["model"]["templates"] = templates
    
    # 4. Add data flow information
    uppaal_model["model"]["data_flow"] = data_flow_info
    
    # 5. System declaration
    uppaal_model["model"]["system"] = create_system_declaration(templates)
    
    return uppaal_model


def extract_data_flow(nested_actions, parts):
    """Extract data flow dependencies between actions"""
    parameters = {}
    dependencies = []
    
    for action in nested_actions:
        action_name = action['name']
        
        # Process outputs
        for param in action.get('params', []):
            if param['direction'] == 'out':
                param_id = f"{action_name}.{param['name']}"
                parameters[param_id] = {
                    "id": param_id,
                    "action": action_name,
                    "parameter": param['name'],
                    "direction": "out",
                    "type": infer_type(param),
                    "global_variable": f"v_{action_name}_{param['name']}",
                    "produced_by": None,  # Will be filled when creating templates
                    "consumed_by": []
                }
            
            # Process inputs
            elif param['direction'] == 'in':
                param_id = f"{action_name}.{param['name']}"
                default = param.get('default')
                
                if default and default.get('type') == 'qualified_id':
                    # This is a data dependency
                    source = default['value']  # e.g., "search.empty_location"
                    source_parts = source.split('.')
                    
                    if len(source_parts) == 2:
                        source_action = source_parts[0]
                        source_param = source_parts[1]
                        source_id = f"{source_action}.{source_param}"
                        
                        # Use the same variable as the source
                        parameters[param_id] = {
                            "id": param_id,
                            "action": action_name,
                            "parameter": param['name'],
                            "direction": "in",
                            "type": infer_type(param),
                            "global_variable": f"v_{source_action}_{source_param}",
                            "source": source_id
                        }
                        
                        # Add dependency
                        dependencies.append({
                            "from": source_id,
                            "to": param_id,
                            "variable": f"v_{source_action}_{source_param}",
                            "type": "output_to_input"
                        })
                else:
                    # Literal value input
                    parameters[param_id] = {
                        "id": param_id,
                        "action": action_name,
                        "parameter": param['name'],
                        "direction": "in",
                        "type": infer_type(param),
                        "literal_value": default.get('value') if default else None,
                        "source": "literal"
                    }
    
    return {
        "parameters": parameters,
        "dependencies": dependencies
    }


def infer_type(param):
    """Infer UPPAAL type from parameter"""
    name = param.get('name', '').lower()
    default = param.get('default')
    
    if 'status' in name:
        return 'int'
    elif default:
        if default.get('type') == 'string':
            return 'int'  # UPPAAL doesn't support strings
        elif default.get('type') == 'number':
            return 'int'  # UPPAAL doesn't support floating-point
        elif default.get('type') == 'qualified_id':
            # For references like search.empty_location, try to infer from source
            # For now, default to int
            return 'int'
    
    # Default to int unless we have explicit type info
    return 'int'


def create_global_declarations(data_flow_info, mission):
    """Create global declarations for UPPAAL"""
    variables = []
    constants = []
    clocks = ["timeNow"]
    typedefs = []  # Track custom types that need typedef
    
    # Add mission-level attributes as global variables/constants
    for attr in mission.get('attributes', []):
        attr_name = attr['name']
        attr_type = attr.get('type', 'int')
        
        if 'fields' in attr:
            # Complex structured attribute like Coordinate
            # Add typedef if not a basic type
            if attr_type not in ['int', 'bool', 'clock'] and attr_type not in [t['name'] for t in typedefs]:
                # Create typedef based on the fields
                typedef = create_typedef(attr_type, attr['fields'])
                if typedef:
                    typedefs.append(typedef)
            
            variables.append({
                "name": attr_name,
                "type": attr_type,
                "initial": None,
                "fields": attr['fields'],
                "comment": f"Mission attribute"
            })
        elif 'value' in attr:
            # Simple attribute with a value - treat as variable
            value = attr['value']
            variables.append({
                "name": attr_name,
                "type": convert_sysml_type(attr_type),
                "initial": value,
                "comment": "Mission attribute"
            })
    
    # Add variables from data flow
    seen_vars = set()
    for param_id, param_info in data_flow_info['parameters'].items():
        var_name = param_info.get('global_variable')
        
        # Only add output variables (inputs share the same variable)
        if var_name and var_name not in seen_vars and param_info['direction'] == 'out':
            variables.append({
                "name": var_name,
                "type": param_info['type'],
                "initial": 0 if param_info['type'] == 'int' else None,
                "comment": f"Output from {param_info['action']}.{param_info['parameter']}"
            })
            seen_vars.add(var_name)
    
    return {
        "clocks": clocks,
        "variables": variables,
        "constants": constants,
        "typedefs": typedefs
    }


def create_typedef(type_name, fields):
    """Create a typedef definition for a structured type"""
    if type_name == 'Coordinate' or set(fields.keys()) == {'X', 'Y', 'Z'}:
        # Coordinate type: struct with X, Y, Z
        return {
            "name": type_name,
            "kind": "struct",
            "fields": [
                {"name": "X", "type": "int"},
                {"name": "Y", "type": "int"},
                {"name": "Z", "type": "int"}
            ]
        }
    else:
        # Generic struct based on the fields
        struct_fields = []
        for field_name, field_value in fields.items():
            # Infer type from value
            if isinstance(field_value, bool):
                field_type = "bool"
            elif isinstance(field_value, (int, float)):
                field_type = "int"
            else:
                field_type = "int"  # Default
            struct_fields.append({"name": field_name, "type": field_type})
        
        return {
            "name": type_name,
            "kind": "struct",
            "fields": struct_fields
        }


def convert_sysml_type(sysml_type):
    """Convert SysML type to UPPAAL type"""
    type_map = {
        'Number': 'int',
        'Real': 'int',     # UPPAAL doesn't support floating-point
        'Integer': 'int',
        'Boolean': 'bool',
        'String': 'string',
    }
    # Return the type as-is if not in map (could be custom type like Coordinate)
    return type_map.get(sysml_type, sysml_type)


def create_channels(nested_actions):
    """Create synchronization channels for each action"""
    channels = []
    
    for action in nested_actions:
        action_name = action['name']
        
        channels.append({
            "name": f"{action_name}_req",
            "type": "broadcast",
            "comment": f"Request {action_name} action"
        })
        
        channels.append({
            "name": f"{action_name}_done",
            "type": "binary",
            "comment": f"{action_name} action completed"
        })
    
    return channels


def create_controller_template(flow, nested_actions, data_flow_info):
    """Create the Controller template that orchestrates the flow"""
    states = []
    transitions = []
    state_counter = 0
    state_map = {}  # Map state names to their IDs to avoid duplicates
    
    def get_or_create_state(name, **kwargs):
        """Get existing state ID or create new state"""
        nonlocal state_counter
        if name in state_map:
            return state_map[name]
        
        state_id = f"S{state_counter}"
        states.append({
            "id": state_id,
            "name": name,
            "invariant": kwargs.get("invariant"),
            **{k: v for k, v in kwargs.items() if k not in ["invariant"]}
        })
        state_map[name] = state_id
        state_counter += 1
        return state_id
    
    # Start state
    start_state = get_or_create_state("Start", initial=True, committed=True)
    prev_state = start_state
    
    # Process flow
    for step in flow:
        if isinstance(step, dict):
            if step.get('type') == 'if':
                # Create decision state
                decision_state = get_or_create_state("Decision")
                
                # Transition to decision from previous state
                transitions.append({
                    "from": prev_state,
                    "to": decision_state,
                    "guard": None,
                    "sync": None,
                    "update": []
                })
                
                # If branch
                if step['if_branch']:
                    action_name = step['if_branch'][0]['name']
                    if_state = get_or_create_state(f"Wait_{action_name}")
                    
                    transitions.append({
                        "from": decision_state,
                        "to": if_state,
                        "guard": step['condition'],
                        "sync": f"{action_name}_req!",
                        "update": []
                    })
                
                # Else branch
                if step.get('else_branch'):
                    action_name = step['else_branch'][0]['name']
                    else_state = get_or_create_state(f"Wait_{action_name}")
                    
                    transitions.append({
                        "from": decision_state,
                        "to": else_state,
                        "guard": f"!({step['condition']})",
                        "sync": f"{action_name}_req!",
                        "update": []
                    })
                    
                    prev_state = else_state
                else:
                    prev_state = if_state
                
            else:
                # Regular action
                action_name = step.get('name')
                if action_name:
                    wait_state = get_or_create_state(f"Wait_{action_name}")
                    
                    # Transition to request action
                    transitions.append({
                        "from": prev_state,
                        "to": wait_state,
                        "guard": None,
                        "sync": f"{action_name}_req!",
                        "update": []
                    })
                    
                    # Create next state for receiving done
                    next_state = get_or_create_state(f"After_{action_name}")
                    
                    # Transition on done
                    transitions.append({
                        "from": wait_state,
                        "to": next_state,
                        "guard": None,
                        "sync": f"{action_name}_done?",
                        "update": []
                    })
                    
                    prev_state = next_state
    
    # Done state
    done_state = get_or_create_state("Done")
    
    transitions.append({
        "from": prev_state,
        "to": done_state,
        "guard": None,
        "sync": None,
        "update": []
    })
    
    return {
        "name": "Controller",
        "type": "orchestrator",
        "local_declarations": {
            "clocks": [],
            "variables": []
        },
        "states": states,
        "transitions": transitions
    }


def create_agent_template(part, nested_actions, data_flow_info):
    """Create a template for an agent (vehicle)"""
    part_name = part['name']
    part_type = part['type']
    performs = part.get('performs', [])
    
    # Extract attributes
    attributes = {}
    for attr in part.get('attributes', []):
        attributes[attr['name']] = attr.get('value')
    
    # Create states
    states = [{
        "id": "Idle",
        "name": "Idle",
        "initial": True,
        "invariant": None
    }]
    
    # Create transitions
    transitions = []
    local_clock = f"clock_{part_name}"
    
    # For each action this agent performs
    for action_name in performs:
        # Find the action definition
        action = next((a for a in nested_actions if a['name'] == action_name), None)
        if not action:
            continue
        
        # Create executing state
        exec_state = f"{action_name.capitalize()}"
        states.append({
            "id": exec_state,
            "name": exec_state,
            "invariant": f"{local_clock} <= 30"  # Default max duration
        })
        
        # Collect outputs to write
        outputs_update = []
        for param in action.get('params', []):
            if param['direction'] == 'out':
                param_id = f"{action_name}.{param['name']}"
                param_info = data_flow_info['parameters'].get(param_id)
                if param_info:
                    var_name = param_info['global_variable']
                    if 'status' in param['name']:
                        outputs_update.append(f"{var_name} = 1")
        
        # Transition: Idle -> Executing
        transitions.append({
            "from": "Idle",
            "to": exec_state,
            "guard": None,
            "sync": f"{action_name}_req?",
            "update": [f"{local_clock} = 0"]
        })
        
        # Transition: Executing -> Idle (or Done for last action)
        is_last_action = (performs.index(action_name) == len(performs) - 1)
        target_state = "Done" if is_last_action else "Idle"
        
        if is_last_action and target_state == "Done":
            states.append({
                "id": "Done",
                "name": "Done",
                "invariant": None
            })
        
        transitions.append({
            "from": exec_state,
            "to": target_state,
            "guard": f"{local_clock} >= 3",  # Default min duration
            "sync": f"{action_name}_done!",
            "update": outputs_update
        })
    
    return {
        "name": part_type,
        "type": "agent",
        "instance": part_name,
        "id": attributes.get('id', '').strip('"'),
        "attributes": {k: v for k, v in attributes.items() if k != 'id'},
        "local_declarations": {
            "clocks": [local_clock],
            "variables": []
        },
        "states": states,
        "transitions": transitions
    }


def create_system_declaration(templates):
    """Create system declaration"""
    instances = []
    
    # Create instances with part names (e.g., forklift_1, drone_1)
    for template in templates:
        if template['type'] == 'orchestrator':
            # Controller uses lowercase instance name
            instances.append({
                "template": template['name'],
                "name": template['name'].lower()
            })
        else:
            # Agents use their part names (e.g., forklift_1, drone_1)
            instances.append({
                "template": template['name'],
                "name": template['instance']
            })
    
    return {
        "instances": instances
    }
