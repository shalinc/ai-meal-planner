import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
    const location = useLocation();

    return (
        <nav className="bg-white shadow sticky top-0 z-10">
            <div className="max-w-5xl mx-auto px-4 py-3 flex gap-4">
                <Link to="/" className="text-green-600 font-semibold hover:underline">🍽 Suggest Meal</Link>
                <Link to="/history" className="text-gray-700 font-semibold hover:underline">📜 Meal History</Link>
            </div>
        </nav>
    );
}
