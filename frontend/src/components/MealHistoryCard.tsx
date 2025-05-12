type Props = {
    entry: any;
};

export default function MealHistoryCard({ entry }: Props) {
    const { title, datetime, nutrition } = entry;

    return (
        <div className="border rounded-lg p-4 shadow-sm bg-gray-50">
            <h2 className="text-lg font-semibold text-green-700 mb-1">{title}</h2>
            <p className="text-sm text-gray-500 mb-2">{new Date(datetime).toLocaleString()}</p>

            {nutrition && (
                <div className="text-sm text-gray-700 grid grid-cols-2 sm:grid-cols-4 gap-2">
                    <p>🔥 {nutrition.calories} cal</p>
                    <p>💪 {nutrition.protein} protein</p>
                    <p>🥔 {nutrition.carbs} carbs</p>
                    <p>🧈 {nutrition.fat} fat</p>
                </div>
            )}
        </div>
    );
}
