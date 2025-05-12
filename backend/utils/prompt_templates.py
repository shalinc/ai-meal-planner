def build_meal_prompt(calories: int, protein: int, diet: str, meal_type: str,
                      exclude: list, goal: str, effort: str, pantry=None) -> str:
    """
    Builds a prompt string for the AI meal planner based on user inputs.
    """
    goal_desc = {
        "bulk": "high in calories and protein to support muscle gain",
        "cut": "lower in calories but high in protein and fiber to support fat loss",
        "maintain": "balanced in calories, protein, and nutrients"
    }[goal]

    effort_desc = {
        "easy": "quick and simple to prepare",
        "moderate": "with moderate cooking effort",
        "chef": "more elaborate with complex flavors"
    }[effort]

    base = (
        f"Act as a nutritionist and suggest a {diet} {meal_type} with around {calories} calories and at least "
        f"{protein} grams of protein. The meal should be {goal_desc} and {effort_desc}."
    )

    if pantry:
        base += (
            f" You have the following ingredients available: {', '.join(pantry)}."
            f" You may use these if appropriate, but it's okay to include common ingredients as well."
        )

    if exclude:
        base += f" Avoid: {', '.join(exclude)}."

    base += (" Include ingredients and rough preparation steps. Adjust the nutrition values if needed."
             " Include Indian recipies as well whenever possible, doesn't have to be always.")

    base += " Also give estimated macros (calories, protein, carbs, fat) with the same naming convention clearly at the end."

    return base
