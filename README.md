# Healthcare-AI-Explorer
Overview
Healthcare AI Explorer is a Streamlit-based web application that enables users to analyze healthcare data efficiently using AI-powered SQL query generation.

Key Features:
Upload CSV files and store data in SQLite

Generate SQL queries from natural language questions using Gemini Pro or GPT-4

Execute queries and display results instantly

Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/Sailaxmi2000/Healthcare-AI-Explorer.git
cd Healthcare-AI-Explorer
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Keys
Create a .env file in the project root and add:

ini
Copy
Edit
GEMINI_API_KEY=your_google_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
5️⃣ Run the Application
sh
Copy
Edit
streamlit run app.py
The application will launch in your browser.

Project Structure
bash
Copy
Edit
📂 Healthcare-AI-Explorer/
│-- 📄 app.py              # Main application  
│-- 📄 requirements.txt    # Dependencies  
│-- 📄 .env                # API keys (ignored in Git)  
│-- 📄 README.md           # Project documentation  
License
This project is licensed under the MIT License.
