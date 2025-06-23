# 🤖 Custom AI Chatbot

A fully customizable, modern chatbot application built with Streamlit and FastAPI, seamlessly integrating Groq and OpenAI language models to create intelligent, personalized AI agents.

---

## Features

- Supports multiple AI providers: Groq and OpenAI  
- Customize agent behavior with system prompts  
- Optional real-time web search integration via Tavily API  
- Interactive and user-friendly frontend using Streamlit  
- Fast, scalable backend powered by FastAPI  
- Easy configuration through environment variables  

---

## Getting Started

### Prerequisites

- Python 3.11 or higher  
- Git  

### Installation

```bash
git clone https://github.com/M-Adam-Khan/Custom-AI-Chatbot.git
cd Custom-AI-Chatbot
python -m venv venv

# Activate virtual environment:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
Configuration
Create a .env file in the project root and add your API keys:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
You can obtain these keys from the respective service providers.

Running the Application
Start the backend server:

bash
Copy
Edit
uvicorn backend:app --reload --port 5000
In a new terminal, start the frontend:

bash
Copy
Edit
streamlit run frontend.py
Open your web browser and go to:

arduino
Copy
Edit
http://localhost:8501
Project Structure
bash
Copy
Edit
├── backend.py          # FastAPI backend server
├── frontend.py         # Streamlit frontend application
├── ai_agent.py         # Integration logic with AI providers and tools
├── requirements.txt    # Python dependencies
├── .gitignore          # Files and folders ignored by Git
├── README.md           # Project documentation (this file)
└── .env.example        # Example environment variable file
Contributing
Contributions, bug reports, and feature requests are welcome!
Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Contact
M. Adam Khan
GitHub: M-Adam-Khan
Email: your.email@example.com

⭐ If you find this project useful, please give it a star!

yaml
Copy
Edit

---
