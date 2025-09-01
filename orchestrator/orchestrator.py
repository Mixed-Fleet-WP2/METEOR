import json
import paho.mqtt.client as mqtt
from rich import print as rprint

def run_orchestration(data):
    mission = data[0]
    flow_order = [step['name'] for step in mission['flow']]
    actions = {a['name']: a for a in mission['nested_actions']}
    parts = mission['parts']

    # Build a mapping from action name to actor name
    action_to_actor = {}
    for part in parts:
        for action_name in part.get('performs', []):
            action_to_actor[action_name] = part['name']

    rprint(f":arrow_right: [bold cyan]Flow order:[/bold cyan] {flow_order}")
    rprint(":busts_in_silhouette: [bold green]Actors and their actions:[/bold green]")
    for part in parts:
        rprint(f":bust_in_silhouette: [bold yellow]{part['name']}[/bold yellow] performs [italic]{part['performs']}[/italic]")

    broker = 'localhost'
    port = 2883
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    current_index = 0
    outputs = {}  # Store outputs from all previous actions

    def resolve_input(param, action, mission):
        default = param.get('default', {})
        if default.get('type') == 'qualified_id':
            ref = default.get('value')
            value = outputs.get(ref, None)
            rprint(f":mag: [bold cyan]Resolved input[/bold cyan] [italic]{param['name']}[/italic] from [italic]{ref}[/italic]: {value}")
            return value
        elif default.get('type') == 'attribute_ref':
            attr_name = default.get('value')
            # Search in action attributes first
            attrs = action.get('attributes') or []
            for attr in attrs:
                if attr['name'] == attr_name:
                    if 'fields' in attr:
                        rprint(f":mag: [bold cyan]Resolved input[/bold cyan] [italic]{param['name']}[/italic] from action attribute [italic]{attr_name}[/italic]: {attr['fields']}")
                        return attr['fields']
                    elif 'value' in attr:
                        rprint(f":mag: [bold cyan]Resolved input[/bold cyan] [italic]{param['name']}[/italic] from action attribute [italic]{attr_name}[/italic]: {attr['value']}")
                        return attr['value']
            # If not found, search in mission attributes
            mission_attrs = mission.get('attributes') or []
            for attr in mission_attrs:
                if attr['name'] == attr_name:
                    if 'fields' in attr:
                        rprint(f":mag: [bold cyan]Resolved input[/bold cyan] [italic]{param['name']}[/italic] from mission attribute [italic]{attr_name}[/italic]: {attr['fields']}")
                        return attr['fields']
                    elif 'value' in attr:
                        rprint(f":mag: [bold cyan]Resolved input[/bold cyan] [italic]{param['name']}[/italic] from mission attribute [italic]{attr_name}[/italic]: {attr['value']}")
                        return attr['value']
            rprint(f":warning: [bold yellow]Attribute '{attr_name}' not found for input '{param['name']}'[/bold yellow]")
            return None
        return default.get('value', None)

    def publish_action(index):
        if index >= len(flow_order):
            rprint(":white_check_mark: [bold green]All actions completed.[/bold green]")
            return
        action_name = flow_order[index]
        action = actions.get(action_name)
        actor = action_to_actor.get(action_name, "unknown")
        if not action:
            rprint(f":warning: [bold yellow]Action {action_name} not found.[/bold yellow]")
            return
        # Build command_arguments from 'in' params
        command_arguments = {}
        for param in action.get('params', []):
            if param['direction'] == 'in':
                command_arguments[param['name']] = resolve_input(param, action, mission)
        # Build prerequisites (could be previous actions, or empty if not tracked)
        prerequisites = []
        if index > 0:
            prerequisites = [flow_order[index-1]]
        payload = {
            "executing_robot": actor,
            "command": action_name,
            "command_arguments": command_arguments,
            "action_id": index + 1,
            "prerequisites": prerequisites
        }
        topic = f"{actor}/{action_name}"
        client.publish(topic, json.dumps(payload))
        rprint(f":rocket: [bold blue]Published to[/bold blue] [italic]{topic}[/italic]: {payload}")
        
    def on_connect(client, userdata, flags, rc, properties=None):
        rprint(":satellite: [bold magenta]Connected to broker.[/bold magenta]")
        publish_action(current_index)
        action_name = flow_order[current_index]
        actor = action_to_actor.get(action_name, "unknown")
        client.subscribe(f"{actor}/{action_name}/feedback")
        rprint(f":bell: [bold cyan]Subscribed to[/bold cyan] [italic]{actor}/{action_name}/feedback[/italic]")

    def on_message(client, userdata, msg):
        nonlocal current_index  
        action_name = flow_order[current_index]
        actor = action_to_actor.get(action_name, "unknown")
        expected_out_params = [
            param for param in actions[action_name].get('params', [])
            if param['direction'] == 'out'
        ]
        try:
            feedback = json.loads(msg.payload.decode())
            # Check feedback matches expected 'out' params
            rprint(f":inbox_tray: [bold yellow]Received feedback on[/bold yellow] [italic]{msg.topic}[/italic]: {feedback}")
            for param in expected_out_params:
                pname = param['name']
                if pname not in feedback:
                    rprint(f":warning: [bold red]Feedback missing expected output '{pname}' for action '{action_name}'[/bold red]")
                else:
                    # Optionally check type if 'default' has 'type'
                    expected_type = param['default']['type'] if param.get('default') and isinstance(param['default'], dict) else None
                    value = feedback[pname]
                    if expected_type:
                        # Simple type check (number, string, etc.)
                        if expected_type == "number" and not isinstance(value, (int, float)):
                            rprint(f":warning: [bold yellow]Type mismatch for '{pname}': expected number, got {type(value).__name__}[/bold yellow]")
                        elif expected_type == "string" and not isinstance(value, str):
                            rprint(f":warning: [bold yellow]Type mismatch for '{pname}': expected string, got {type(value).__name__}[/bold yellow]")
            # Store outputs
            for param in expected_out_params:
                outputs[f"{action_name}.{param['name']}"] = feedback.get(param['name'])
                rprint(f":package: [bold green]Stored output[/bold green] [italic]{action_name}.{param['name']}[/italic]: {feedback.get(param['name'])}")
        except Exception as e:
            rprint(f":x: [bold red]Error parsing feedback:[/bold red] {e}")
        current_index += 1
        publish_action(current_index)
        if current_index < len(flow_order):
            next_action = flow_order[current_index]
            next_actor = action_to_actor.get(next_action, "unknown")
            client.subscribe(f"{next_actor}/{next_action}/feedback")
            rprint(f":bell: [bold cyan]Subscribed to[/bold cyan] [italic]{next_actor}/{next_action}/feedback[/italic]")

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.loop_forever()