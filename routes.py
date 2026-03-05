from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from gemini_generator import generate_workout_gemini

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(request: Request, goal: str = Form(...), intensity: str = Form(...)):
    
    plan = generate_workout_gemini(goal, intensity)

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "plan": plan}
    ) 