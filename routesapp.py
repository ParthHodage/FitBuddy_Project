from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to FitBuddy AI Fitness Generator"}

@router.post("/generate-workout")
def generate_workout(goal: str, intensity: str):
    return {
        "goal": goal,
        "intensity": intensity,
        "workout_plan": "AI generated workout plan will appear here"
    }

@router.get("/nutrition-tip")
def nutrition_tip(goal: str):
    return {
        "goal": goal,
        "tip": "Eat high protein foods and stay hydrated."
    } 