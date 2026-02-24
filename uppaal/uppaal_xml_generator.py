"""
UPPAAL XML Generator
Converts UPPAAL JSON model to UPPAAL XML format
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom


def generate_uppaal_xml(uppaal_model):
    """
    Generate UPPAAL XML from the UPPAAL JSON model
    
    Args:
        uppaal_model: Dictionary containing the UPPAAL model structure
        
    Returns:
        str: Formatted UPPAAL XML string
    """
    
    # Create root element with DOCTYPE
    nta = ET.Element('nta')
    
    # Add global declaration
    declaration = ET.SubElement(nta, 'declaration')
    declaration.text = generate_global_declarations(uppaal_model['model'])
    
    # Add templates
    for template_data in uppaal_model['model']['templates']:
        generate_template(nta, template_data)
    
    # Add system declaration
    system = ET.SubElement(nta, 'system')
    system.text = generate_system_declaration(uppaal_model['model'])
    
    # Add queries section (empty for now, can be populated later)
    queries = ET.SubElement(nta, 'queries')
    
    # Convert to string with proper formatting
    xml_str = ET.tostring(nta, encoding='unicode')
    
    # Pretty print with minidom
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="\t")
    
    # Add DOCTYPE declaration
    lines = pretty_xml.split('\n')
    if lines[0].startswith('<?xml'):
        lines.insert(1, "<!DOCTYPE nta PUBLIC '-//Uppaal Team//DTD Flat System 1.6//EN' 'http://www.it.uu.se/research/group/darts/uppaal/flat-1_6.dtd'>")
    
    return '\n'.join(lines)


def generate_global_declarations(model):
    """Generate global declarations section"""
    decls = []
    
    decls.append("// Global declarations")
    decls.append("")
    
    global_decls = model['global_declarations']
    
    # Add type definitions from typedefs
    if global_decls.get('typedefs'):
        decls.append("// Type definitions")
        for typedef in global_decls['typedefs']:
            if typedef['kind'] == 'struct':
                # Generate struct typedef
                field_decls = []
                for field in typedef['fields']:
                    field_decls.append(f"{field['type']} {field['name']}")
                fields_str = "; ".join(field_decls) + ";"
                decls.append(f"typedef struct {{ {fields_str} }} {typedef['name']};")
        decls.append("")
    
    # Add channels
    if model['channels']:
        decls.append("// Synchronization channels")
        for channel in model['channels']:
            if channel['type'] == 'broadcast':
                decls.append(f"broadcast chan {channel['name']};")
            else:
                decls.append(f"chan {channel['name']};")
        decls.append("")
    
    # Add global clocks
    global_decls = model['global_declarations']
    if global_decls['clocks']:
        decls.append("// Global clocks")
        clock_decls = ", ".join(global_decls['clocks'])
        decls.append(f"clock {clock_decls};")
        decls.append("")
    
    # Add constants first (before variables)
    if global_decls.get('constants'):
        decls.append("// Constants")
        for const in global_decls['constants']:
            const_type = const['type']  # Use type as-is
            value = format_value(const['value'], const['type'])
            decls.append(f"const {const_type} {const['name']} = {value};")
        decls.append("")
    
    # Add global variables
    if global_decls['variables']:
        decls.append("// Global variables")
        for var in global_decls['variables']:
            var_type = var['type']  # Use type as-is (could be custom type)
            comment = f"  // {var.get('comment', '')}" if var.get('comment') else ""
            
            # Handle custom struct types with field initialization
            if var.get('fields'):
                fields = var['fields']
                # Build initialization list from fields
                field_values = []
                for typedef in global_decls.get('typedefs', []):
                    if typedef['name'] == var_type:
                        for field in typedef['fields']:
                            field_name = field['name']
                            field_val = int(fields.get(field_name, 0))
                            field_values.append(str(field_val))
                        break
                else:
                    # Fallback if typedef not found
                    field_values = [str(int(v)) for v in fields.values()]
                
                init_str = ", ".join(field_values)
                decls.append(f"{var_type} {var['name']} = {{ {init_str} }};{comment}")
            elif var.get('initial') is not None:
                init_val = f" = {format_value(var['initial'], var['type'])}"
                decls.append(f"{var_type} {var['name']}{init_val};{comment}")
            else:
                decls.append(f"{var_type} {var['name']};{comment}")
        decls.append("")
    
    # Add status flag
    decls.append("// Status flags")
    decls.append("bool mission_complete = false;")
    decls.append("")
    
    return "\n".join(decls)


def convert_type(type_str):
    """Convert JSON type to UPPAAL type"""
    type_map = {
        'int': 'int',
        'string': 'string',
        'double': 'int',  # UPPAAL doesn't support floating-point, use int
        'float': 'int',   # UPPAAL doesn't support floating-point, use int
        'bool': 'bool'
    }
    # Custom types (like typedefs) pass through as-is
    return type_map.get(type_str, type_str)


def format_value(value, type_str):
    """Format value based on type"""
    if value is None:
        return '0'
    if type_str == 'bool':
        return 'true' if value else 'false'
    if type_str == 'string':
        # Quote string values
        return f'"{value}"'
    # Convert all numeric values to int for UPPAAL
    if isinstance(value, float):
        return str(int(value))
    return str(value)


def generate_template(nta, template_data):
    """Generate a template element"""
    template = ET.SubElement(nta, 'template')
    
    # Template name
    name = ET.SubElement(template, 'name')
    name.text = template_data['name']
    
    # Local declarations
    if template_data.get('local_declarations'):
        declaration = ET.SubElement(template, 'declaration')
        declaration.text = generate_local_declarations(template_data['local_declarations'])
    
    # Create locations (states)
    # Calculate positions in a grid layout
    x_start, y_start = -1000, -300
    x_spacing, y_spacing = 250, 200
    
    for idx, state in enumerate(template_data['states']):
        location = ET.SubElement(template, 'location')
        location.set('id', state['id'])
        
        # Position in a flow layout
        x_pos = x_start + (idx % 4) * x_spacing
        y_pos = y_start + (idx // 4) * y_spacing
        
        location.set('x', str(x_pos))
        location.set('y', str(y_pos))
        
        # Location name
        loc_name = ET.SubElement(location, 'name')
        loc_name.set('x', str(x_pos - 10))
        loc_name.set('y', str(y_pos - 34))
        loc_name.text = state['name']
        
        # Invariant
        if state.get('invariant'):
            invariant = ET.SubElement(location, 'label')
            invariant.set('kind', 'invariant')
            invariant.set('x', str(x_pos - 10))
            invariant.set('y', str(y_pos + 10))
            invariant.text = state['invariant']
        
        # Committed state
        if state.get('committed'):
            ET.SubElement(location, 'committed')
    
    # Mark initial location
    for state in template_data['states']:
        if state.get('initial'):
            init = ET.SubElement(template, 'init')
            init.set('ref', state['id'])
            break
    
    # Create transitions
    for trans in template_data['transitions']:
        transition = ET.SubElement(template, 'transition')
        
        # Source and target
        source = ET.SubElement(transition, 'source')
        source.set('ref', trans['from'])
        
        target = ET.SubElement(transition, 'target')
        target.set('ref', trans['to'])
        
        # Guard
        if trans.get('guard'):
            guard = ET.SubElement(transition, 'label')
            guard.set('kind', 'guard')
            guard.text = trans['guard']
        
        # Synchronization
        if trans.get('sync'):
            sync = ET.SubElement(transition, 'label')
            sync.set('kind', 'synchronisation')
            sync.text = trans['sync']
        
        # Update/Assignment
        if trans.get('update') and trans['update']:
            update_text = ', '.join(trans['update'])
            if update_text:  # Only add if not empty
                update = ET.SubElement(transition, 'label')
                update.set('kind', 'assignment')
                update.text = update_text
    
    return template


def generate_local_declarations(local_decls):
    """Generate local declarations for a template"""
    decls = []
    
    # Local clocks
    if local_decls.get('clocks'):
        decls.append("// Local clocks")
        clock_list = ", ".join(local_decls['clocks'])
        decls.append(f"clock {clock_list};")
        decls.append("")
    
    # Local variables
    if local_decls.get('variables'):
        decls.append("// Local variables")
        for var in local_decls['variables']:
            var_type = convert_type(var.get('type', 'int'))
            init_val = ""
            if var.get('initial') is not None:
                init_val = f" = {var['initial']}"
            decls.append(f"{var_type} {var['name']}{init_val};")
        decls.append("")
    
    return "\n".join(decls) if decls else ""


def generate_system_declaration(model):
    """Generate system declaration"""
    decls = []
    
    decls.append("// System declaration")
    
    # Generate instantiations: instanceName = TemplateName();
    instance_names = []
    for instance in model['system']['instances']:
        template_name = instance['template']
        instance_name = instance['name']
        decls.append(f"{instance_name} = {template_name}();")
        instance_names.append(instance_name)
    
    decls.append("")
    
    # Create system line with instance names
    decls.append(f"system {', '.join(instance_names)};")
    
    return "\n".join(decls)


def save_uppaal_xml(uppaal_model, output_path):
    """
    Generate and save UPPAAL XML to file
    
    Args:
        uppaal_model: Dictionary containing the UPPAAL model
        output_path: Path to save the XML file
        
    Returns:
        str: Path to saved file
    """
    xml_content = generate_uppaal_xml(uppaal_model)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    return output_path
