# Healthcare AI Explorer  

## Overview  
Healthcare AI Explorer is a **Streamlit-based** web application that enables users to analyze healthcare data efficiently using **AI-powered SQL query generation**.  

### Key Features  
- Upload **CSV files** and store data in **SQLite**  
- Generate **SQL queries from natural language questions** using **Gemini Pro** or **GPT-4**  
- Execute **queries** and display results instantly  

## Installation & Setup  

### 1. Clone the Repository  

git clone https://github.com/Sailaxmi2000/Healthcare-AI-Explorer.git
cd Healthcare-AI-Explorer


###** 2.** Create a Virtual Environment **** 
python -m venv venv
Activate the virtual environment
###**3.Install Dependencies
**
## Windows
venv\Scripts\activate

## Mac/Linux
source venv/bin/activate'

### 4.Set Up API Keys

Create a .env file in the project root and add:
GEMINI_API_KEY=your_google_gemini_api_key
OPENAI_API_KEY=your_openai_api_key

###5. Run the Application
streamlit run app.py

###Project Structure
Healthcare-AI-Explorer/
│-- app.py              # Main application  
│-- requirements.txt    # Dependencies  
│-- .env                # API keys (ignored in Git)  
│-- README.md           # Project documentation

###Dependencies
Ensure you have the following installed:
Python 3.8+
Streamlit
Pandas
SQLite
OpenAI API
Google Generative AI API
Python Dotenv

###Install all dependencies with:
pip install -r requirements.txt

###How It Works
1️⃣ Upload a CSV file – The data is stored in an SQLite database.
2️⃣ Choose an AI Model – Select between Gemini Pro and GPT-4.
3️⃣ Ask a question – Enter a natural language question related to your data.
4️⃣ Get SQL Query & Results – The AI generates an SQL query, executes it, and displays the results.


