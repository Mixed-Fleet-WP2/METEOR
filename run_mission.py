import sys
import os
import json
from datetime import datetime
from grammar.parse_model import parse_model
from orchestrator.orchestrator import run_orchestration


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
    if len(sys.argv) != 2:
        print("Usage: python run_mission.py <model_file.mxf>")
        sys.exit(1)

    model_file = sys.argv[1]
    if not os.path.isfile(model_file):
        print(f"File not found: {model_file}")
        sys.exit(1)

    actions = parse_model(model_file)
    print("Parsed actions")


    save_actions_history(actions)
    run_orchestration(actions)

if __name__ == "__main__":
    main()