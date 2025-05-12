import { useEffect, useState } from "react";
import { getMealHistory } from "../api/historyApi";
import MealHistoryCard from "../components/MealHistoryCard";

export default function MealHistoryPage() {
    const [mealType, setMealType] = useState("dinner");
    const [entries, setEntries] = useState<any[]>([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        fetchHistory();
    }, [mealType]);

    const fetchHistory = async () => {
        setLoading(true);
        try {
            const data = await getMealHistory(mealType);
            setEntries(data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 px-4 py-8">
            <div className="max-w-4xl mx-auto bg-white p-6 rounded-xl shadow-md space-y-6">
                <div className="flex justify-between items-center">
                    <h1 className="text-2xl font-bold text-gray-800">📜 Meal History</h1>
                    <select
                        value={mealType}
                        onChange={(e) => setMealType(e.target.value)}
                        className="border p-2 rounded-md focus:ring-2 focus:ring-green-500"
                    >
                        <option value="breakfast">Breakfast</option>
                        <option value="lunch">Lunch</option>
                        <option value="dinner">Dinner</option>
                    </select>
                </div>

                {loading ? (
                    <p className="text-gray-600">Loading...</p>
                ) : entries.length === 0 ? (
                    <p className="text-gray-500 italic">No meals found for this category.</p>
                ) : (
                    <div className="grid gap-4">
                        {entries.map((e, i) => (
                            <MealHistoryCard key={i} entry={e} />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}
