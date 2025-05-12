from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.meals import router as meals_router
from backend.routes.pantry import router as pantry_router

app = FastAPI(title="AI Meal Planner API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(meals_router, prefix="/api/meals")
app.include_router(pantry_router, prefix="/api/pantry")