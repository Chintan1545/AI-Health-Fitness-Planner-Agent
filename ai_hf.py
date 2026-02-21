import os
import streamlit as st
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq


# Load Environment Variables

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()


# Initialize Groq Model

try:
    groq_model = Groq(
        id="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY
    )
except Exception as e:
    st.error(f"Model Initialization Failed: {e}")
    st.stop()


# Streamlit Config

st.set_page_config(
    page_title="AI Health & Fitness Planner ",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ AI Health & Fitness Planner")
st.markdown("Generate personalized diet and fitness plans.")


# Session State

if "dietary_plan" not in st.session_state:
    st.session_state.dietary_plan = ""
    st.session_state.fitness_plan = ""
    st.session_state.qa_history = []


# User Inputs

st.header("👤 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 10, 100)
    height = st.number_input("Height (cm)", 100.0, 250.0)
    activity_level = st.selectbox(
        "Activity Level",
        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
    )

with col2:
    weight = st.number_input("Weight (kg)", 20.0, 300.0)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    goal = st.selectbox(
        "Fitness Goal",
        ["Lose Weight", "Gain Muscle", "Stay Fit", "Endurance"]
    )


# Generate Plans

if st.button("🎯 Generate Plan", use_container_width=True):

    with st.spinner("Generating your personalized plans..."):

        user_profile = f"""
        Age: {age}
        Height: {height} cm
        Weight: {weight} kg
        Sex: {sex}
        Activity Level: {activity_level}
        Goal: {goal}
        """

        
        # Dietary Agent
        
        dietary_agent = Agent(
            name="Dietary Expert",
            role="Provides personalized dietary plans",
            model=groq_model,
            instructions=[
                "Create a detailed 1-day meal plan.",
                "Include breakfast, lunch, dinner, snacks.",
                "Explain why it matches the user's goal.",
                "Keep structured formatting."
            ]
        )

        
        # Fitness Agent
        
        fitness_agent = Agent(
            name="Fitness Expert",
            role="Provides personalized workout routines",
            model=groq_model,
            instructions=[
                "Create a detailed workout routine.",
                "Include warm-up, main workout, cool-down.",
                "Explain benefits of exercises.",
                "Make it practical and safe."
            ]
        )

        try:
            dietary_response = dietary_agent.run(user_profile)
            fitness_response = fitness_agent.run(user_profile)

            st.session_state.dietary_plan = dietary_response.content
            st.session_state.fitness_plan = fitness_response.content

        except Exception as e:
            st.error(f"Error generating plan: {e}")


# Display Plans

if st.session_state.dietary_plan:
    st.header("🥗 Personalized Dietary Plan")
    st.markdown(st.session_state.dietary_plan)

if st.session_state.fitness_plan:
    st.header("💪 Personalized Fitness Plan")
    st.markdown(st.session_state.fitness_plan)


# Q&A Section

if st.session_state.dietary_plan:
    st.header("❓ Ask Questions About Your Plan")

    question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if question:

            context = f"""
            Dietary Plan:
            {st.session_state.dietary_plan}

            Fitness Plan:
            {st.session_state.fitness_plan}

            User Question: {question}
            """

            qa_agent = Agent(model=groq_model)

            try:
                answer = qa_agent.run(context).content
                st.session_state.qa_history.append((question, answer))
            except Exception as e:
                st.error(f"Error: {e}")


# Q&A History

if st.session_state.qa_history:
    st.header("💬 Q&A History")

    for q, a in st.session_state.qa_history:
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")