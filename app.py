from flask import Flask, render_template
from flask import Flask, render_template, request, jsonify
from digital_twin_embeder import answer_query

app = Flask(__name__)


@app.route("/")
def home():
    # Career objective: AI/ML first, then software dev
    career_objective = (
        "To build reliable, explainable AI and machine learning systems that solve real-world problems, "
        "and to complement them with robust software engineering so they can be deployed, used, and improved in practice."
    )

    # Projects (you can edit or add more later)
    projects = [
        {
            "name": "Brick Kiln Detection and Temporal Change Analysis",
            "category": "AI / Computer Vision",
            "description": "Designed a YOLO-based detection and temporal change detection pipeline over multi-year satellite imagery to monitor brick kilns.",
            "tech_stack": ["Python", "PyTorch", "YOLOv8", "LSTM / ConvLSTM"],
            "specialities": [
                "End-to-end ML pipeline design",
                "Temporal modeling for change detection",
                "Evaluation and performance tuning",
            ],
            "link": "#",
        },
        {
            "name": "Human Activity Recognition (UCI HAR)",
            "category": "Machine Learning",
            "description": "Classified human activities using smartphone sensor data with feature engineering and dimensionality reduction.",
            "tech_stack": ["Python", "Pandas", "Scikit-Learn", "PCA"],
            "specialities": [
                "Signal preprocessing and EDA",
                "Feature engineering and PCA",
                "Multi-class model training and evaluation",
            ],
            "link": "#",
        },
        {
            "name": "Document Extractor and Classifier",
            "category": "NLP / Automation",
            "description": "Built a pipeline to extract text from PDFs and classify them using classical ML and transformer-based approaches.",
            "tech_stack": ["Python", "BERT", "Scikit-Learn"],
            "specialities": [
                "Document preprocessing and structure detection",
                "Transformer-based text classification",
                "Automation of report generation",
            ],
            "link": "#",
        },
        {
            "name": "Next-Token Text Generator",
            "category": "Generative AI",
            "description": "Implemented a mini language model to generate the next token in a sequence and deployed it as an interactive demo.",
            "tech_stack": ["Python", "Deep Learning"],
            "specialities": [
                "Sequence modeling fundamentals",
                "Training and evaluating language models",
                "Building a simple interactive interface",
            ],
            "link": "#",
        },
        {
            "name": "POS Inventory Management System",
            "category": "Software Development",
            "description": "Developed a Java-based POS system with MySQL backend for inventory and billing.",
            "tech_stack": ["Java", "JDBC", "MySQL", "Swing"],
            "specialities": [
                "Desktop UI in Java",
                "Relational database design",
                "CRUD-based business logic",
            ],
            "link": "#",
        },
        {
            "name": "Course and Attendance Management Tools",
            "category": "Software Development",
            "description": "Built Java desktop tools for course management and timetable-based attendance tracking.",
            "tech_stack": ["Java", "JDBC", "MySQL", "Swing"],
            "specialities": [
                "Form-based desktop UIs",
                "DB integration and validation",
                "Time-table aware attendance logic",
            ],
            "link": "#",
        },
    ]

    # Techstack: tools / technologies
    techstack = {
        "Programming Languages": ["Python", "Java", "C", "C++", "SQL", "JavaScript"],
        "Web and Backend": ["HTML", "CSS", "Flask", "JSP", "Java Spring", "JDBC"],
        "Data and ML Libraries": [
            "NumPy",
            "Pandas",
            "Scikit-Learn",
            "TensorFlow",
            "PyTorch",
            "Matplotlib",
            "Ultralytics YOLO",
        ],
        "Databases and Tools": ["MySQL", "Git", "GitHub", "GroqCloud", "OpenAI SDK"],
    }

    # Skills: what you can do
    skills = [
        "Artificial Intelligence and Machine Learning (end-to-end pipelines)",
        "Deep Learning for vision and text",
        "Computer Vision: detection, super-resolution, reconstruction",
        "Natural Language Processing and document understanding",
        "Agentic AI: AI agents, tool use, and workflows",
        "Desktop software development using Java (Swing, JDBC, MySQL)",
        "Integrating IoT devices (sensors, microcontrollers) with custom software",
        "Product thinking: problem framing, roadmapping, and experimentation",
    ]

    # Work experience
    experience = [
        {
            "role": "Summer Research Intern",
            "org": "IIT Gandhinagar",
            "period": "May 2025 – July 2025",
            "location": "Gandhinagar, India",
            "highlights": [
                "Worked on computer vision models (YOLO, ConvLSTM, Vision Transformers) for monitoring brick kilns.",
                "Designed a change-detection pipeline across multi-year satellite imagery.",
                "Built a hand-validation and ground-truth generation tool to speed up labeling.",
            ],
        }
    ]

    # Education timeline (you will later add per-sem details into these dicts)
    education = [
        {
            "label": "10th Standard",
            "institution": "St. Kabir School, Ahmedabad",
            "year": "2020",
            "details": "GSEB Board",
        },
        {
            "label": "12th Standard (PCM)",
            "institution": "Divyapath Higher Secondary School, Ahmedabad",
            "year": "2022",
            "details": "GSHSEB Board",
        },
        {
            "label": "B.E. Computer Engineering (AI & ML Honors)",
            "institution": "L.D. College of Engineering, GTU",
            "year": "2022 – 2026",
            "details": "You can add semester-wise CPI here later.",
        },
        {
            "label": "Visiting Student",
            "institution": "IIT Gandhinagar",
            "year": "Aug 2025 – Nov 2025",
            "details": "Focused on ML and AI research projects.",
        },
        {
            "label": "BSc in Data Science and Applications",
            "institution": "IIT Madras (Online)",
            "year": "Ongoing",
            "details": "Data science, statistics, and applications.",
        },
    ]

    # Contact info
    contact = {
        "email": "rpshah51174@gmail.com",
        "github": "https://github.com/RuddhiPS",
        "linkedin": "https://www.linkedin.com/in/ruddhips",
        "location": "Ahmedabad, India",
    }

    return render_template(
        "index.html",
        career_objective=career_objective,
        projects=projects,
        techstack=techstack,
        skills=skills,
        experience=experience,
        education=education,
        contact=contact,
    )

@app.post("/api/ask-twin")
def api_ask_twin():
    """
    API endpoint for the Digital Twin chat.
    Expects JSON: { "question": "..." }
    Returns JSON: { "answer": "..." }
    """
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or data.get("message") or "").strip()

    if not question:
        return jsonify({"error": "Empty question"}), 400

    try:
        answer = answer_query(question)
        return jsonify({"answer": answer})
    except Exception as e:
        app.logger.exception("Digital Twin error")
        return jsonify({"error": "Internal error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
