# ATS Tracking System

# Introduction

ATS Tracking System is an advanced Streamlit application that leverages the power of Large Language Models (LLM) and OpenAI to provide comprehensive resume analysis. It excels at summarizing resumes, evaluating strengths, identifying weaknesses, and offering personalized improvement suggestions, while also recommending suitable job titles.ATS Tracking System simplifies the job-seeking process by providing users with detailed insights to enhance their career opportunities.

# Key Technologies and Skills
Python
LangChain
LLM
google-generativeai
pdf2image
Streamlit

# Installation

pip install PyPDF2
pip install langchain
pip install streamlit
pip install google.generativeai

Clone the repository:git clone https://github.com/Thangam-11/ATS-Tracking-system.git

pip install -r requirements.txt

streamlit run app.py

Access the app in your browser at http://localhost:8501.

# Features
# Easy User Experience

The ATS Tracking System offers a user-friendly interface that allows users to effortlessly upload their resumes and benefit from powerful resume analysis features.

Text Extraction: Uses the PyPDF2 library to extract text from uploaded resumes, initiating a thorough analysis.

# Comprehensive Resume Analysis
 Summary:Provides a quick, comprehensive overview of resumes, emphasizing qualifications, key experience, skills, projects, and achievements.
 
 Strengths: Highlights qualifications, experience, and accomplishments, providing job seekers with a competitive edge.
 
 Weaknesses:Pinpoints areas for improvement and offers tailored suggestions to transform weaknesses into strengths.Suggestions.
 
Recommends personalized job titles aligned with the user's qualifications and resume content, optimizing the job search experience.

Percentage Match: Evaluates the percentage match between the resume and the job description.

# How It Works

The application uses Google Generative AI to analyze resume content:

model = genai.GenerativeModel("gemini-1.5-flash")

# Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

# License
This project is licensed under the MIT License. Please review the LICENSE file for more details.

# Contact
📧 Email: thangamani1128@gmail.com
🌐 LinkedIn: linkedin.com/in/thangarasu-m-

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any que
