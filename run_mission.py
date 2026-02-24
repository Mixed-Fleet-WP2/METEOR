import sys
import os
import json
from datetime import datetime
from grammar.parse_model import parse_model
from orchestrator.orchestrator import run_orchestration
from uppaal.uppaal_xml_generator import save_uppaal_xml


def save_actions_history(actions):
    history_dir = "history"
    os.makedirs(history_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"actions_{timestamp}.json"
    filepath = os.path.join(history_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(actions, f, indent=2, ensure_ascii=False)
    print(f"Saved actions to {filepath}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_mission.py <model_file.sysml> [--uppaal] [--run]")
        print("  --uppaal: Generate UPPAAL-compatible JSON and XML")
        print("  --run: Run the orchestrator (requires MQTT broker)")
        sys.exit(1)

    model_file = sys.argv[1]
    generate_uppaal = "--uppaal" in sys.argv
    run_orchestrator = "--run" in sys.argv
    
    if not os.path.isfile(model_file):
        print(f"File not found: {model_file}")
        sys.exit(1)

    # Parse SysML format
    parsedFile = parse_model(model_file, output_format='sysml')
    print("Parsed model (SysML format)")
    print(f"Package: {parsedFile.get('package', 'N/A')}")
    print(f"Imports: {len(parsedFile.get('imports', []))}")
    print(f"Actions: {len(parsedFile.get('actions', []))}")

    save_actions_history(parsedFile)
    
    # Generate UPPAAL format if requested
    if generate_uppaal:
        try:
            uppaal_model = parse_model(model_file, output_format='uppaal')
            
            # Save UPPAAL JSON to history
            history_dir = "history"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            uppaal_json_filename = f"uppaal_{timestamp}.json"
            uppaal_json_filepath = os.path.join(history_dir, uppaal_json_filename)
            
            with open(uppaal_json_filepath, "w", encoding="utf-8") as f:
                json.dump(uppaal_model, f, indent=2, ensure_ascii=False)
            
            # Save UPPAAL XML to uppaal_models directory
            uppaal_models_dir = "uppaal_models"
            os.makedirs(uppaal_models_dir, exist_ok=True)
            
            # Get model name from package or use default
            model_name = uppaal_model.get('package', 'model')
            uppaal_xml_filename = f"{model_name}_{timestamp}.xml"
            uppaal_xml_filepath = os.path.join(uppaal_models_dir, uppaal_xml_filename)
            
            save_uppaal_xml(uppaal_model, uppaal_xml_filepath)
            
            print(f"\nGenerated UPPAAL model:")
            print(f"  Templates: {len(uppaal_model['model']['templates'])}")
            for template in uppaal_model['model']['templates']:
                print(f"    - {template['name']} ({template['type']}): {len(template['states'])} states")
            print(f"  Channels: {len(uppaal_model['model']['channels'])}")
            print(f"  Global variables: {len(uppaal_model['model']['global_declarations']['variables'])}")
            print(f"  Saved JSON to: {uppaal_json_filepath}")
            print(f"  Saved XML to: {uppaal_xml_filepath}")
        except Exception as e:
            print(f"Error generating UPPAAL format: {e}")
            import traceback
            traceback.print_exc()
    
    # Only run orchestrator if --run flag is provided
    if run_orchestrator:
        print("\nStarting orchestrator...")
        run_orchestration(parsedFile["actions"])
    else:
        print("\nSkipping orchestrator (use --run to execute mission)")

if __name__ == "__main__":
    main()