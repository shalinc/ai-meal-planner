from backend.models.meal_models import MealRequest

def build_prompt(request: MealRequest, pantry: list) -> str:
    """
    Builds a prompt string for the AI meal planner based on user inputs.
    """
    goal_desc = {
        "bulk": "high in calories and protein to support muscle gain",
        "cut": "lower in calories but high in protein and fiber to support fat loss",
        "maintain": "balanced in calories, protein, and nutrients"
    }[request.goal]

    effort_desc = {
        "easy": "quick and simple to prepare",
        "moderate": "with moderate cooking effort",
        "chef": "more elaborate with complex flavors"
    }[request.effort]

    base = (
        f"Act as a chef plus nutritionist and suggest a {request.diet} {request.meal} with around {request.calories} calories and at least "
        f"{request.protein} grams of protein. The suggested recipie should be {goal_desc} and {effort_desc}. If the meal is a breakfast, suggest accordingly."
    )

    if pantry:
        base += (
            f" I have the following ingredients in my pantry: {', '.join(pantry)}. "
            f"You may use these. Make sure the suggested recipie is a valid combination, and you don't have to use every ingredient from the pantry, use "
            f" what goes well for a recipie, and it's okay to include common ingredients as well."
        )

    if request.exclude:
        base += f" Avoid: {', '.join(request.exclude)}."

    base += (" Adjust the nutrition values if needed. Include Indian recipies as well whenever possible, "
             "doesn't have to be always. Include ingredients and preparation steps.")

    base += (" JSON should include recipe, ingredients (list of {\"name\": <string>, \"quantity\": <string>})"
             " instructions (list of steps), nutritionInformation (calories formatted as value kcal, protein in grams, "
             "carbohydrates in grams, fat in grams) property values in double quoted strings. "
             " Respond ONLY with a valid JSON object. Do not include any commentary, explanation, markdown, or formatting outside the JSON.")

    return base