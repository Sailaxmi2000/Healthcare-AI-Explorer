import streamlit as st
import pandas as pd
import sqlite3
import google.generativeai as genai
import openai  # For OpenAI API
from dotenv import load_dotenv
import os

# Load API key for both Gemini Pro and GPT-4
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get Gemini Pro response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([prompt, question])
    return response.text.strip()

# Function to get GPT-4 response
def get_openai_response(question, prompt):
    response = openai.Completion.create(
        model="gpt-4",  # Use GPT-4 model
        prompt=prompt + "\n" + question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to execute SQL queries
def get_response(sql):
    conn = sqlite3.connect("Health.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.commit()
    except Exception as e:
        rows = [("Error:", str(e))]  # Show SQL errors
    conn.close()
    
    return rows

# Streamlit UI
st.set_page_config(page_title="Healthcare Data Explorer", layout="wide")

# Custom CSS for better layout
st.markdown(
    """
    <style>
        .block-container {
            max-width: 90% !important;
            padding: 20px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a custom container with two equal halves
left_col, right_col = st.columns(2)  # Equal width columns

# --- Left Column (File Upload & Model Selection) ---
with left_col:
    st.header("📂 Upload CSV & Model Selection")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # Store data in SQLite
        conn = sqlite3.connect("Health.db")
        cursor = conn.cursor()

        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Health (
                Pregnancies INTEGER,
                Glucose INTEGER,
                BloodPressure INTEGER,
                SkinThickness INTEGER,
                Insulin INTEGER,
                BMI REAL,
                DiabetesPedigreeFunction REAL,
                Age INTEGER,
                Outcome INTEGER
            );
        """)
        
        df.to_sql("Health", conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()

        st.success("✅ CSV uploaded and data stored successfully!")
        st.subheader("Preview of Uploaded Data:")
        st.write(df.head())

    model_choice = st.selectbox("Select AI Model", ["Gemini Pro", "GPT-4"])

# --- Right Column (Title & Ask Question Section) ---
with right_col:
    st.title("📊 Healthcare Data Analysis with AI")

    st.header("🤖 Ask Questions About Your Data")
    question = st.text_input("Enter your question:")
    submit = st.button("Generate Query & Get Results")

    prompt = """
    You are an expert in converting English questions to SQL queries.
    The SQL database is named Health with columns: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, and Outcome.
    
    Examples:
    1. "How many records are there?" → SQL: SELECT COUNT(*) FROM Health;
    2. "List all patients with glucose levels higher than 140?" → SQL: SELECT * FROM Health WHERE Glucose > 140;
    3. "Find the average BMI of patients?" → SQL: SELECT AVG(BMI) FROM Health;
    4. "Retrieve records of patients older than 50?" → SQL: SELECT * FROM Health WHERE Age > 50;
    5. "Show all diabetic patients?" → SQL: SELECT * FROM Health WHERE Outcome = 1;
    
    Do NOT include ```sql or ``` in the output.
    """

    if submit:
        if question:
            if model_choice == "Gemini Pro":
                generated_query = get_gemini_response(question, prompt)
            else:
                generated_query = get_openai_response(question, prompt)
            
            st.subheader("Generated SQL Query:")
            st.code(generated_query, language="sql")

            data = get_response(generated_query)

            st.subheader("Query Results:")
            for row in data:
                st.write(row)
        else:
            st.error("❌ Please enter a valid question!")
