import { BrowserRouter, Routes, Route } from "react-router-dom";
import MealSuggestPage from "./pages/MealSuggestPage";
import MealHistoryPage from "./pages/MealHistoryPage";
import Navbar from "./components/Navbar";

function App() {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path="/" element={<MealSuggestPage />} />
                <Route path="/history" element={<MealHistoryPage />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
