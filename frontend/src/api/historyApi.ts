import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000/api",
});

export const getMealHistory = async (meal: string) => {
    const res = await API.get(`/meals/history`, {
        params: { meal },
    });
    return res.data;
};
