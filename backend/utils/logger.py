from datetime import datetime
import os
import json
import uuid

def log_meal(prompt: str, response: str, args, nutrition=None, model: str = "llama3", feedback: str = None, log_dir="logs"):
    """
    Logs the meal suggestion to a structured daily log file split by meal type.
    Each log entry is a single JSON object in .jsonl format.
    """
    os.makedirs(log_dir, exist_ok=True)

    # Normalize meal type and prepare log filename
    meal_type = args.meal.lower().replace(" ", "_")
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"{meal_type}_log_{date_str}.jsonl"
    log_file = os.path.join(log_dir, log_filename)

    log_entry = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "model": model,
        "meal_type": args.meal,
        "calories": args.calories,
        "protein": args.protein,
        "diet": args.diet,
        "exclude": args.exclude,
        "prompt": prompt,
        "response": response.strip(),
        "feedback": feedback,  # Can be "liked", "disliked", or None,
        "nutrition": nutrition
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
