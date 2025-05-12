// src/components/MealCard.tsx
import {useState} from "react";

type Props = {
    meal: any;
};

export default function MealCard({ meal }: Props) {
    const [error, setError] = useState("");

    let parsed;
    try {
        parsed = meal?.response ? JSON.parse(meal.response) : null;
    } catch (err: any) {
        setError("Something went wrong. Please try again.")
    }

    return (
        <div className="mt-6 p-4 border rounded shadow bg-white">
            <h2 className="text-xl font-bold text-green-700 mb-2">
                {parsed?.recipe || "Suggested Meal"}
            </h2>
            {error && (
                <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mt-4 rounded">
                    <p className="text-yellow-700 text-sm mb-2">{error}</p>
                </div>
            )}

            {parsed?.ingredients && (
                <div>
                    <h3 className="font-semibold">Ingredients:</h3>
                    <ul className="list-disc pl-6">
                        {parsed.ingredients.map((item: any, i: number) => (
                            <li key={i}>
                                {item.quantity} of {item.name}
                            </li>
                        ))}
                    </ul>
                </div>
            )}

            {parsed?.instructions && (
                <div className="mt-4">
                    <h3 className="font-semibold">Instructions:</h3>
                    <ol className="list-decimal pl-6">
                        {parsed.instructions.map((step: string, i: number) => (
                            <li key={i}>{step}</li>
                        ))}
                    </ol>
                </div>
            )}

            {parsed?.nutritionInformation && (
                <div className="mt-4 text-sm text-gray-700">
                    <h3 className="font-semibold">Nutrition Info:</h3>
                    <p>🔥 Calories: {parsed.nutritionInformation.calories}</p>
                    <p>💪 Protein: {parsed.nutritionInformation.protein}</p>
                    <p>🥔 Carbs: {parsed.nutritionInformation.carbohydrates}</p>
                    <p>🧈 Fat: {parsed.nutritionInformation.fat}</p>
                </div>
            )}
        </div>
    );
}
