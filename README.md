# 🥗 AI Meal Planner

A full-stack AI-powered meal planner that suggests meals based on your macro goals and preferences. Built with **FastAPI**, **LLaMA3 (via Ollama)**, and **React + Tailwind CSS**.

---

## 📦 Getting Started (Local Setup)

This app has two parts:

- `backend/` → FastAPI + LLaMA for meal suggestions
- `frontend/` → React + Tailwind UI

---

### ✅ 1. Clone the repo

```bash
git clone https://github.com/shalinc/ai-meal-planner.git
cd ai-meal-planner
```

---

### ✅ 2. Set up the Backend

#### Requirements:
- Python 3.10+
- [Ollama](https://ollama.com) installed
- LLaMA3 model downloaded (`ollama run llama3`)

#### Steps:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Ensure llama3 model is available
ollama run llama3

# Start the API server
uvicorn app:app --reload
```

> Backend runs at `http://localhost:8000`

---

### ✅ 3. Set up the Frontend

#### Requirements:
- Node.js 18+
- Yarn

#### Steps:

```bash
cd ../frontend
yarn install
yarn start
```

> Frontend runs at `http://localhost:3000`

---

### 🔧 Environment Notes (Optional)

- Backend uses local models via Ollama and logs meals to `logs/`
- You can configure exclusions, effort, and meal type via the UI

---

## ✨ Features

- ✅ Suggest meals with macro targets
- ✅ Exclude ingredients
- ✅ Avoid repeating meals (title + ingredients)
- ✅ Meal history by type
- ✅ Retry + loading indicators
- ✅ Responsive UI with Tailwind

---

## 🚧 Coming Soon

- 🌟 Favorites and dashboard
- 📊 Weekly macro summaries
- 📂 Pantry management
- 🔁 Real-time streaming with token-based UI

