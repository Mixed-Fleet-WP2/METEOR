"""Test UPPAAL XML generation"""
import json
from grammar.parse_model import parse_model
from uppaal.uppaal_xml_generator import save_uppaal_xml
from datetime import datetime
import os

# Parse model
print("Parsing model...")
uppaal_model = parse_model("sample.sysml", output_format='uppaal')

print(f"Templates: {len(uppaal_model['model']['templates'])}")
for template in uppaal_model['model']['templates']:
    print(f"  - {template['name']}: {len(template['states'])} states, {len(template['transitions'])} transitions")

# Save XML
print("\nGenerating XML...")
uppaal_models_dir = "uppaal_models"
os.makedirs(uppaal_models_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_name = uppaal_model.get('package', 'model')
xml_path = os.path.join(uppaal_models_dir, f"{model_name}_{timestamp}.xml")

save_uppaal_xml(uppaal_model, xml_path)
print(f"✓ XML saved to: {xml_path}")

# Also save JSON for comparison
json_path = os.path.join(uppaal_models_dir, f"{model_name}_{timestamp}.json")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(uppaal_model, f, indent=2, ensure_ascii=False)
print(f"✓ JSON saved to: {json_path}")

print("\nDone!")
