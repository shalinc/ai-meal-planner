import { useState } from "react";
import { suggestMeal } from "../api/mealApi";
import MealCard from "../components/MealCard";

export default function MealSuggestPage() {
    const [form, setForm] = useState({
        calories: 600,
        protein: 30,
        diet: "vegetarian",
        meal: "lunch",
        exclude: [],
        goal: "maintain",
        effort: "easy",
    });

    const [excludeInput, setExcludeInput] = useState("");
    const [result, setResult] = useState<any>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        const parsedExcludes = excludeInput
            .split(",")
            .map((e) => e.trim())
            .filter(Boolean);

        setLoading(true);
        try {
            const data = await suggestMeal({ ...form, exclude: parsedExcludes });
            setResult(data);
        } catch (err: any) {
            const status = err?.response?.status;
            const message = err?.response?.data?.detail;

            if (status === 409) {
                setError(message || "This meal was already suggested recently.");
            } else {
                setError("Something went wrong. Please try again.");
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 px-4 py-8">
            <div className="max-w-2xl mx-auto bg-white shadow-md rounded-xl p-6 space-y-6">
                <h1 className="text-2xl font-bold text-gray-800">🍽 Suggest a Meal</h1>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Calories</label>
                        <input
                            name="calories"
                            type="number"
                            value={form.calories}
                            onChange={handleChange}
                            className="w-full p-2 border rounded-md focus:ring-2 focus:ring-green-500"
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Protein (g)</label>
                        <input
                            name="protein"
                            type="number"
                            value={form.protein}
                            onChange={handleChange}
                            className="w-full p-2 border rounded-md focus:ring-2 focus:ring-green-500"
                        />
                    </div>

                    <div className="md:col-span-2">
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Exclude Ingredients <span className="text-xs text-gray-400">(comma-separated)</span>
                        </label>
                        <input
                            type="text"
                            placeholder="e.g. onion, garlic"
                            value={excludeInput}
                            onChange={(e) => setExcludeInput(e.target.value)}
                            className="w-full p-2 border rounded-md focus:ring-2 focus:ring-yellow-500"
                        />
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Diet</label>
                        <select
                            name="diet"
                            value={form.diet}
                            onChange={handleChange}
                            className="w-full p-2 border rounded-md"
                        >
                            <option value="vegetarian">Vegetarian</option>
                            <option value="vegan">Vegan</option>
                        </select>
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Meal Type</label>
                        <select
                            name="meal"
                            value={form.meal}
                            onChange={handleChange}
                            className="w-full p-2 border rounded-md"
                        >
                            <option value="breakfast">Breakfast</option>
                            <option value="lunch">Lunch</option>
                            <option value="dinner">Dinner</option>
                        </select>
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Goal</label>
                        <select
                            name="goal"
                            value={form.goal}
                            onChange={handleChange}
                            className="w-full p-2 border rounded-md"
                        >
                            <option value="cut">Cut</option>
                            <option value="bulk">Bulk</option>
                            <option value="maintain">Maintain</option>
                        </select>
                    </div>

                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Effort</label>
                        <select
                            name="effort"
                            value={form.effort}
                            onChange={handleChange}
                            className="w-full p-2 border rounded-md"
                        >
                            <option value="easy">Easy</option>
                            <option value="moderate">Moderate</option>
                            <option value="chef">Chef</option>
                        </select>
                    </div>
                </div>

                <div className="pt-2">
                    <button
                        onClick={handleSubmit}
                        disabled={loading}
                        className="bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-2 rounded-md shadow transition duration-200"
                    >
                        {loading ? "Generating..." : "Suggest Meal"}
                    </button>
                </div>

                {result && (
                    <div className="mt-6">
                        <MealCard meal={result} />
                    </div>
                )}
                {error && (
                    <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mt-4 rounded">
                        <p className="text-yellow-700 text-sm mb-2">{error}</p>
                        <button
                            onClick={handleSubmit}
                            className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-sm"
                        >
                            Try another suggestion
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
}
