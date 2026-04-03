from fastapi import FastAPI
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Bano Qabil Chatbot API")
#  static folder (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")
class UserMessage(BaseModel):
    text: str
def get_response(user_input: str):
    user_input = user_input.lower()

    courses = {
        "python": {
            "keywords": ["python"],
            "details": (
                " Python Programming Course\n"
                "- Duration: 3 months\n"
                "- Level: Beginner to Advanced\n"
                "- Topics: Basics, OOP, APIs, FastAPI\n"
                "- Career Paths: Backend Developer, Data Analyst"
            )
        },
        "web": {
            "keywords": ["web", "web development", "frontend", "backend"],
            "details": (
                "Web Development Course\n"
                "- Duration: 3 months\n"
                "- Topics: HTML, CSS, JavaScript, React\n"
                "- Backend: Django / Node.js\n"
                "- Career Paths: Web Developer"
            )
        },
        "ai": {
            "keywords": ["ai", "artificial intelligence", "machine learning"],
            "details": (
                " Artificial Intelligence Course\n"
                "- Duration: 3 months\n"
                "- Topics: Python, ML, Neural Networks\n"
                "- Tools: TensorFlow, Scikit-learn\n"
                "- Career Paths: AI Engineer"
            )
        },
        "graphic": {
            "keywords": ["graphic", "design", "graphic design"],
            "details": (
                " Graphic Design Course\n"
                "- Duration: 3 months\n"
                "- Tools: Photoshop, Illustrator\n"
                "- Skills: Branding, UI Design\n"
                "- Career Paths: Graphic Designer"
            )
        }
    }

    for course in courses.values():
        for keyword in course["keywords"]:
            if keyword in user_input:
                return course["details"]


    if "course" in user_input or "courses" in user_input:
        return "We offer Python, Web Development, AI, and Graphic Design."

    if "fee" in user_input or "free" in user_input:
        return "Bano Qabil training is 100% FREE with a refundable security deposit."

    if "hi" in user_input or "hello" in user_input:
        return "Assalam-o-Alaikum! Welcome to Bano Qabil."

    return "Sorry, I didn't understand. Ask about a specific course like Python or AI."
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/chat")
def chat(message: UserMessage):
    reply = get_response(message.text)
    return {"response": reply}

