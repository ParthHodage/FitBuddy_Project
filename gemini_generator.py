import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-pro")

def generate_workout_gemini(goal, intensity):
    
    prompt = f"""
    Create a personalized 7-day workout plan.

    Goal: {goal}
    Intensity: {intensity}

    Each day should include:
    - Warm-up (5-10 minutes)
    - Main workout with sets and reps
    - Cooldown or recovery tip
    """

    response = model.generate_content(prompt)

    return response.text