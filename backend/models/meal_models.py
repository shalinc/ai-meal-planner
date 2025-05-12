from pydantic import BaseModel
from typing import List, Optional, Dict


class MealRequest(BaseModel):
    calories: int
    protein: int
    diet: str
    meal: str
    exclude: Optional[List[str]] = []
    goal: str
    effort: str


class MealResponse(BaseModel):
    prompt: str
    response: str
    nutrition: Optional[Dict[str, int]]
