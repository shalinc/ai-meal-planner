# services/logger_service.py
from datetime import datetime, timedelta
import os
import json
import uuid
import glob
from backend.models.meal_models import MealRequest

def log_meal(prompt: str, response: str, request: MealRequest, nutrition: dict,
             model: str = "llama3", log_dir="logs", ingredients=None, title=None):
    os.makedirs(log_dir, exist_ok=True)

    meal_type = request.meal.lower().replace(" ", "_")
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %I:%M %p")

    log_file = os.path.join(log_dir, f"{meal_type}_log_{date_str}.jsonl")

    log_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": date_str,
        "datetime": now.isoformat(),
        "model": model,
        "meal_type": request.meal,
        "calories": request.calories,
        "protein": request.protein,
        "diet": request.diet,
        "exclude": request.exclude,
        "goal": request.goal,
        "effort": request.effort,
        "prompt": prompt,
        "response": response.strip(),
        "nutrition": nutrition,
        "ingredients": ingredients or [],
        "title": title
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def was_ingredient_combo_used(meal_type: str, ingredients: list, log_dir="logs") -> bool:
    current = set(ingredients)
    files = glob.glob(f"{log_dir}/{meal_type.lower()}_log_*.jsonl")

    for file in files:
        with open(file, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    if set(entry.get("ingredients", [])) == current:
                        return True
                except:
                    continue

    return False

def was_meal_already_suggested(
        meal_type: str,
        ingredients: list,
        title: str,
        days: int = 7,
        log_dir: str = "logs"
) -> bool:
    current_ingredients = set(ingredients)
    normalized_title = title.lower().strip()

    # Only include files from the last N days
    cutoff = datetime.now() - timedelta(days=days)
    files = glob.glob(f"{log_dir}/{meal_type.lower()}_log_*.jsonl")

    for file in files:
        with open(file, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    entry_date = datetime.fromisoformat(entry.get("datetime", "2000-01-01"))

                    if entry_date < cutoff:
                        continue

                    # Ingredient match
                    if set(entry.get("ingredients", [])) == current_ingredients:
                        return True

                    # Title match (loose)
                    if entry.get("title", "").lower().strip() == normalized_title:
                        return True

                except Exception as e:
                    continue

    return False

