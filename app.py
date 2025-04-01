from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

# Function to get Gemini response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([prompt, question])
    return response.text.strip()
    

# Function to execute SQL query
def sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    return rows

# Define SQL Prompt for Gemini
prompt = """
You are an expert in converting English questions to SQL queries.
The SQL database is named STUDENT with columns: NAME, CLASS, SECTION, Marks.

Examples:
1. "How many records are there?" → SQL: SELECT COUNT(*) FROM STUDENT;
2. "List students in Data Science class?" → SQL: SELECT * FROM STUDENT WHERE CLASS='Data Science';

Do NOT include ```sql or ``` in the output.
"""

# Streamlit UI'
st.set_page_config(page_title="Retrieve SQL Query")
st.header("Gemini-powered SQL Query Generator")

question = st.text_input("Enter your question:", key="input")
submit = st.button("Generate Query")

if submit:
    if question:
        # Get SQL query from Gemini AI
        generated_query = get_gemini_response(question, prompt)

        # Display generated query
        st.subheader("Generated SQL Query:")
        st.code(generated_query, language="sql")

        # Execute SQL query
        data = sql_query(generated_query, "student.db")

        # Display SQL query results
        st.subheader("Query Results:")
        for row in data:
            st.write(row)
    else:
        st.error("Please enter a valid question!")
