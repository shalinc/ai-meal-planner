from fastapi import APIRouter, HTTPException, Body
from typing import List
import json
import os

router = APIRouter()

PANTRY_FILE = "backend/data/pantry.json"

@router.get("")
def get_pantry():
    if not os.path.exists(PANTRY_FILE):
        return {"ingredients": []}
    with open(PANTRY_FILE, "r") as f:
        return json.load(f)

@router.post("")
def update_pantry(ingredients: List[str] = Body(...)):
    data = {"ingredients": ingredients}
    os.makedirs("data", exist_ok=True)
    with open(PANTRY_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return data
