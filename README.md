# 🏋️ AI Health & Fitness Planner Agent

An AI-powered Health & Fitness Planner built using **Streamlit** and **Groq LLaMA 3.1**.  
This application generates personalized dietary and workout plans based on user profile data and supports follow-up Q&A.

---

## 🚀 Features

- 🥗 Personalized 1-Day Dietary Plan
- 💪 Customized Workout Routine
- 🤖 Multi-Agent Architecture (Diet Expert + Fitness Expert)
- 🔐 Secure API Key Management using `.env`
- 💬 Context-Aware Q&A System
- ⚡ Ultra-fast inference using Groq LLaMA 3.1

---

## 🧠 Architecture Overview

```

User Input
↓
Streamlit UI
↓
Groq LLaMA 3.1 Model
↓
Diet Agent + Fitness Agent
↓
Session State Storage
↓
Follow-up Q&A Agent

```

---

## 🛠 Tech Stack

- Python 3.10
- Streamlit
- Groq API
- LLaMA 3.1 (llama-3.1-8b-instant)
- python-dotenv
- Agno (Agent Framework)

---

## 📂 Project Structure

```

ai-health-fitness/
│
├── ai_hf.py
├── .env
├── environment.yml
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Chintan1545/ai-health-fitness.git
cd ai-health-fitness-groq
````

---

### 2️⃣ Create Conda Environment

```bash
conda env create -f environment.yml
conda activate ai-health-groq
```

OR manually:

```bash
conda create -n ai-health-groq python=3.10 -y
conda activate ai-health-groq
pip install streamlit python-dotenv agno
```

---

### 3️⃣ Get Groq API Key

* Go to: [https://console.groq.com](https://console.groq.com)
* Generate your API key

---

### 4️⃣ Create `.env` File

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub.

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 🎯 How It Works

1. User enters profile details (age, height, weight, goal, etc.)
2. A structured prompt is created.
3. Two specialized AI agents are initialized:

   * Dietary Expert
   * Fitness Expert
4. Each agent generates personalized recommendations.
5. Plans are stored in Streamlit session state.
6. Users can ask follow-up questions using contextual Q&A.

---

## 🔐 Security Implementation

* API keys are stored in `.env`
* Loaded using `python-dotenv`
* No hardcoded credentials
* `.env` excluded via `.gitignore`

---

## 💡 Model Used

* `llama-3.3-70b-versatile`

Why this model?

* Ultra-fast inference
* Free-tier friendly
* Optimized for low latency applications

---

## 📈 Future Improvements

* BMI & BMR auto-calculation
* Calorie estimation engine
* Weekly meal planner
* Progress tracking dashboard
* Database integration
* Deployment on Streamlit Cloud

---

## 👤 Author
Chintan Dabhi
MCA (AI & ML) Student
AI/ML & Generative AI Enthusiast
