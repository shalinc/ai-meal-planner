from fastapi import APIRouter, HTTPException
from backend.models.meal_models import MealRequest, MealResponse
from backend.services.prompt_builder import build_prompt
from backend.services.llama_client import call_llama
from backend.services.macro_parser import parse_json_response, extract_macros, extract_ingredient_names
from backend.services.logger_service import log_meal, was_meal_already_suggested
from backend.utils.nutrition_utils import load_pantry
from fastapi import Query
from typing import Optional
import glob
import json

router = APIRouter()

@router.post("/suggest", response_model=MealResponse)
def suggest_meal(request: MealRequest):
    pantry = load_pantry()
    prompt = build_prompt(request, pantry)
    print(prompt)
    response_text = call_llama(prompt)
    print(response_text)
    parsed = parse_json_response(response_text)

    if not parsed:
        return {"response": "⚠️ Failed to parse model response."}

    macros = extract_macros(parsed)
    ingredients = extract_ingredient_names(parsed)
    title = parsed.get("recipe", "Untitled Meal")

    # Check for repetition
    if was_meal_already_suggested(request.meal, ingredients, title, days=7):
        raise HTTPException(
            status_code=409,
            detail=f"⚠️ A similar meal (by ingredients or title) was already suggested in the last 7 days, {title} containing {ingredients}"
        )

    log_meal(prompt, response_text, request, macros, ingredients=ingredients, title=title)

    return MealResponse(
        prompt=prompt,
        response=response_text,
        nutrition=macros
    )

@router.get("/history")
def get_meal_history(meal: str, feedback: Optional[str] = Query(None)):
    files = glob.glob(f"logs/{meal.lower()}_log_*.jsonl")
    results = []

    for file in files:
        with open(file, "r") as f:
            for line in f:
                entry = json.loads(line)
                if feedback:
                    if not entry.get("feedback") or entry["feedback"].get("summary") != feedback:
                        continue
                results.append(entry)

    # Optional: sort by datetime descending
    results.sort(key=lambda x: x.get("datetime", ""), reverse=True)
    return results