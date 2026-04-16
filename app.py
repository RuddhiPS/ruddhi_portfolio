from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests

# from digital_twin_embeder import answer_query

# --------------------
# App initialization
# --------------------
HF_CHAT_URL = "https://RPS11111-digital-twin-inference.hf.space/chat"

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# --------------------
# Home page (HTML)
# --------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    career_objective = (
        "Focused on building production-ready systems by combining my skills in "
        "Machine Learning, Artificial Intelligence, Software Development, and "
        "Product Management, with a strong execution mindset and a focus on real user needs."
    )

    projects = [
        {
            "name": "Portfolio Website with Embedded AI Assitant Bot",
            "category": "AI / Application Development",
            "description": (
                "Built a personal portfolio website with an embedded AI-powered Chat Bot "
                "capable of answering professional, project, and career-related questions."
            ),
            "tech_stack": [
                "Flask",
                "HuggingFace",
                "Sentence Transformers",
                "LLMs",
                "HTML",
                "CSS",
            ],
            "specialities": [
                "AI ChatBot Integrated",
                "Semantic search over personal knowledge base",
                "End-to-end deployment and UI integration",
            ],
            "link": "#",
        },
        {
            "name": "Domain-Specific Question Answering Chatbot",
            "category": "Agentic AI / Expert Systems",
            "description": (
                "Developed an AI-powered question answering system for domain-specific queries, "
                "designed to ensure reliability in critical use cases."
            ),
            "tech_stack": [
                "LLMs",
                "HuggingFace",
                "Sentence Transformers",
                "Streamlit",
                "Gmail API",
            ],
            "specialities": [
                "Knowledge base-driven question answering",
                "Tool-enabled agent capable of triggering email notifications",
                "Hallucination-aware design with fallback to human-in-the-loop",
                "Human-in-the-loop AI system design",
                "Interactive Streamlit demo prototyping",
            ],
            "link": "#",
        },
        {
            "name": "Object Identification and Time-Series Change Analysis",
            "category": "AI / Computer Vision",
            "description": (
                "Designed a YOLO-based detection and temporal change detection pipeline "
                "over multi-year satellite imagery to monitor brick kilns."
            ),
            "tech_stack": ["YOLO", "LSTM / ConvLSTM", "VisionTransformer", "OpenCV"],
            "specialities": [
                "End-to-end ML pipeline design",
                "Improved pipeline accuracy from 85% to 91%",
                "Built a hand-validation application",
                "Evaluation and performance tuning",
            ],
            "link": "#",
        },
    ]

    techstack = {
        "Programming and Scripting Languages": ["Python", "Java", "C", "HTML", "CSS", "SQL"],
        "Frameworks and Libraries": [
            "TensorFlow",
            "PyTorch",
            "Scikit-learn",
            "Flask",
            "Ultralytics",
        ],
        "NLP and LLM": [
            "LLM Training",
            "Fine-tuning",
            "Prompt Engineering",
            "Hugging Face",
        ],
        "Agentic AI": [
            "OpenAI Agents SDK",
            "LangChain",
            "LangGraph",
            "Microsoft AutoGen",
            "n8n",
        ],
        "Computer Vision": [
            "Ultralytics YOLO",
            "Vision Transformer (ViT)",
        ],
        "Developer Tools": ["Git", "GitHub", "Docker", "DVC"],
    }

    experience = [
        {
            "role": "Summer Internship (AIML - Computer Vision)",
            "org": "Sustainability Lab",
            "period": "May 2025 – July 2025",
            "location": "IIT Gandhinagar, India",
            "highlights": [
                "Object Detection and Classification (YOLO, ConvLSTM, ViT)",
                "Time-series change detection on satellite imagery",
                "Built hand-validation and ground-truth tooling",
            ],
        }
    ]

    education = [
        {
            "label": "B.E. Computer Engineering (AI & ML Honours)",
            "institution": "L.D. College of Engineering, GTU",
            "year": "2022 – 2026",
            "details": "9.63/10 CPI",
        },
        {
            "label": "Visiting Student",
            "institution": "IIT Gandhinagar",
            "year": "Aug 2025 – Nov 2025",
            "details": "10/10 CPI",
        },
    ]

    contact = {
        "email": "rpshah51174@gmail.com",
        "github": "https://github.com/RuddhiPS",
        "linkedin": "http://www.linkedin.com/in/ruddhi-shah-05060433b",
        "location": "Ahmedabad, India",
    }

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "career_objective": career_objective,
            "projects": projects,
            "techstack": techstack,
            "experience": experience,
            "education": education,
            "contact": contact,
        },
    )

# --------------------
# API: Digital Twin
# --------------------
class AskTwinRequest(BaseModel):
    question: str | None = None
    message: str | None = None


@app.post("/api/ask-twin")
def api_ask_twin(payload: AskTwinRequest):
    question = (payload.question or payload.message or "").strip()

    if not question:
        raise HTTPException(status_code=400, detail="Empty question")

    try:
        r = requests.post(
            HF_CHAT_URL,
            json={"message": question},
            timeout=20,
        )
        r.raise_for_status()

        data = r.json()
        return {"answer": data.get("reply", "")}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail="Digital Twin service unavailable")
