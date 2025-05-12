// src/api/mealApi.ts
import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000/api", // backend base
});

export const suggestMeal = async (formData: any) => {
    const res = await API.post("/meals/suggest", formData);
    return res.data;
};