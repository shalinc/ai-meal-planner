import json
import os

def load_pantry(filepath="backend/data/pantry.json") -> list:
    if not os.path.exists(filepath):
        print(f"⚠️ Pantry file not found at {filepath}")
        return []

    with open(filepath, "r") as f:
        data = json.load(f)
        return data.get("ingredients", [])
