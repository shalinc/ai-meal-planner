# services/macro_parser.py

import json
import yaml

def parse_json_response(text: str) -> dict | None:
    """
    Pull the first {...} block out of `text` and parse it with PyYAML.
    YAML is a superset of JSON and happily accepts
    un‑quoted scalars like `35g` or `1/2 cup`.
    """
    try:

        return yaml.safe_load(text)
    except yaml.YAMLError as e:
        print(f"⚠️ YAML could not parse the block: {e}")
        return None

def extract_ingredient_names(parsed_json: dict) -> list:
    return sorted({item["name"].lower() for item in parsed_json.get("ingredients", [])})

def extract_macros(parsed_json: dict) -> dict[str, int] | None:
    info = parsed_json.get("nutritionInformation", {})
    try:
        return {
            "calories": int(str(info.get("calories", 0)).replace("kcal", "").strip()),
            "protein": int(str(info.get("protein", "0")).replace("g", "").strip()),
            "carbs": int(str(info.get("carbohydrates", "0")).replace("g", "").strip()),
            "fat": int(str(info.get("fat", "0")).replace("g", "").strip()),
        }
    except Exception as e:
        print(f"⚠️ Macro extraction error: {e}")
        return None

