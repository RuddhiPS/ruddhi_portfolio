from flask import Flask, render_template
from flask import Flask, render_template, request, jsonify
from digital_twin_embeder import answer_query

app = Flask(__name__)


@app.route("/")
def home():
    # Career objective: AI/ML first, then software dev
    career_objective = (
        "Focused on building production-ready systems by combining my skills in Machine Learning, Artificial Intelligence, Software Development, and Product Management, with a strong execution mindset and a focus on real user needs."
    )

    # Projects (you can edit or add more later)
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
                "AI ChatBot Integrated"
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
            "description": "Designed a YOLO-based detection and temporal change detection pipeline over multi-year satellite imagery to monitor brick kilns.",
            "tech_stack": ["YOLO", "LSTM / ConvLSTM","VisionTransformer", "OpenCV"],
            "specialities": [
                "End-to-end ML pipeline design",
                "Proposed a method for change detection using Deep Learning Models thus improving the Machine Learning Pipeline accuracy from 85% to 91%.",
                "Developed a user friendly application to hand validate Ground Truth, thus reducing manual time by half.",
                "Evaluation and performance tuning",
            ],
            "link": "#",
        },
        {
            "name": "Human Activity Recognition (UCI HAR)",
            "category": "Machine Learning",
            "description": "Classified human activities using smartphone sensor data with feature engineering and dimensionality reduction.",
            "tech_stack": ["Feature Engineering", "Scikit-Learn", "PCA" ,"EDA", "Model Training", "Fine-Tuning"],
            "specialities": [
                "Signal preprocessing and EDA",
                "Feature engineering and PCA",
                "Multi-class model training and evaluation",
            ],
            "link": "https://github.com/RuddhiPS/MachineLearning_Regressors/blob/main/Assignment1(HAR_And_DecisionTree)/HAR/Tasks_1_2_3_4_Final.ipynb",
        },
        {
            "name": "Image Classification and Feature Analysis on MNIST Variants",
            "category": "Machine Learning / Computer Vision",
            "description": (
                "Designed and evaluated multiple CNN-based image classifiers on the MNIST and "
                "Fashion-MNIST datasets, with emphasis on feature learning on image Dataset."
            ),
            "tech_stack": [
                "CNNs",
                "PyTorch / TensorFlow",
                "t-SNE",
                "NumPy",
                "Matplotlib",
            ],
            "specialities": [
                "Training and evaluation of multiple CNN architectures",
                "Hyperparameter tuning and performance comparison",
                "Feature space visualization using t-SNE",
                "Model evaluation and error analysis",
            ],
            "link": "https://github.com/RuddhiPS/MachineLearningRegressors_3/blob/main/question3.ipynb",
        },

        {
            "name": "Document Extractor and Classifier",
            "category": "NLP / PDF Automation",
            "description": "Built a pipeline to extract text from PDFs and classify them using classical ML and transformer-based approaches.",
            "tech_stack": ["TFIDF", "BERT", "Scikit-Learn"],
            "specialities": [
                "Transformer-based text classification",
                "Automation of report generation",
                "Built a Web Application integrated with ML Model"
            ],
            "link": "#",
        },
        {
            "name": "Next-Token Text Generator",
            "category": "Generative AI",
            "description": "Implemented a mini language model to generate the next token in a sequence and deployed it as an interactive demo.",
            "tech_stack": ["LLM Training", "Streamlit Demo"],
            "specialities": [
                "Training and evaluating language models",
                "Building a Streamlit interactive interface",
            ],
            "link": "https://machinelearningregreapprs2-dbzjpg4pgu35jgcxesynhn.streamlit.app/",
        },
        {
            "name": "POS Inventory Management System",
            "category": "Software Development",
            "description": "Developed a Java-based POS system with MySQL backend for inventory and billing.",
            "tech_stack": ["Java", "JDBC", "MySQL", "Java Swing"],
            "specialities": [
                "Desktop App in Java",
                "Relational database design",
                "CRUD-based business logic",
            ],
            "link": "#",
        },
        {
            "name": "Course and Attendance Management Tools",
            "category": "Software Development",
            "description": "Built Java desktop tools for course management and timetable-based attendance tracking.",
            "tech_stack": ["Java", "JDBC", "MySQL", "Java Swing"],
            "specialities": [
                "Time-table aware attendance logic",
                "Feature to manage courses by faculties"
            ],
            "link": "#",
        },
    ]

    # Techstack: tools / technologies
    techstack = {
    "Programming and Scripting Languages": [
        "Python", "Java", "C", "HTML", "CSS", "SQL",
    ],
    "Frameworks and Libraries": [
        "TensorFlow", "PyTorch", "Scikit-learn", "Flask", "Ultralytics",
    ],
    "NLP and LLM": [
        "LLM Training", "Fine-tuning", "Prompt Engineering", "Hugging Face",
    ],
    "Agentic AI": [
        "OpenAI Agents SDK", "LangChain", "LangGraph", "Microsoft AutoGen", "n8n"
    ],
    "Computer Vision": [
        "Ultralytics YOLO", "Vision Transformer (ViT)",
    ],
    "Developer Tools": [
        "Git", "GitHub", "Docker", "DVC",
    ],
    }


    # Skills: what you can do
    # skills = [
    #     "Artificial Intelligence and Machine Learning (end-to-end pipelines)",
    #     "Deep Learning for vision and text",
    #     "Computer Vision: detection, super-resolution, reconstruction",
    #     "Natural Language Processing and document understanding",
    #     "Agentic AI: AI agents, tool use, and workflows",
    #     "Desktop software development using Java (Swing, JDBC, MySQL)",
    #     "Integrating IoT devices (sensors, microcontrollers) with custom software",
    #     "Product thinking: problem framing, roadmapping, and experimentation",
    # ]

    # Work experience
    experience = [
        {
            "role": "Summer Internship(AIML - Computer Vision)",
            "org": "Sustainability Lab",
            "period": "May 2025 – July 2025",
            "location": "IIT Gandhinagar, India",
            "highlights": [
                "Object Detection and Classification: Worked on computer vision models (YOLO, ConvLSTM, Vision Transformers).",
                "Timeseries Change Detection: Designed a change-detection pipeline across multi-year satellite images.",
                "Built a hand-validation and ground-truth generation tool to speed up labeling.",
            ],
        }
    ]

    # Education timeline (you will later add per-sem details into these dicts)
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
        {
            "label": "Foundation Level in Data Science and Applications",
            "institution": "IIT Madras (Online)",
            "year": "2025",
            "details": "9.48/10 CPI",
        },

        {
            "label": "12th Standard (PCM)",
            "institution": "Divyapath Higher Secondary School, Ahmedabad",
            "year": "2022",
            "details": "99.93%ile",
        },
        {
            "label": "10th Standard (HSC)",
            "institution": "St. Kabir School, Ahmedabad",
            "year": "2020",
            "details": "99.94%ile",
        },   
    ]

    # Contact info
    contact = {
        "email": "rpshah51174@gmail.com",
        "github": "https://github.com/RuddhiPS",
        "linkedin": "http://www.linkedin.com/in/ruddhi-shah-05060433b",
        "location": "Ahmedabad, India",
    }

    return render_template(
        "index.html",
        career_objective=career_objective,
        projects=projects,
        techstack=techstack,
        # skills=skills,
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
