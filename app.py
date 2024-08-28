from dotenv import load_dotenv  
import streamlit as st 
import os  
from PIL import Image  
import pdf2image   
import google
import google.generativeai as genai 
import io  
import base64  

# Load environment variables
load_dotenv()  

# Set Streamlit page configuration at the top
st.set_page_config(
    page_title="ATS Tracking System",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompts):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, pdf_content[0], prompts])
    return response.text

def input_pdf_setup(upload_file):
    ## Convert the PDF to image
    if upload_file is not None:
        images = pdf2image.convert_from_bytes(upload_file.read())
        first_page = images[0]

        ## Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

# Custom CSS for theme and heading styles
custom_css = """
<style>
    body {
        background-color: #f0f0f0; 
        color: #333333; 
    }
    .stApp {
        background-color: #f0f0f0; 
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #333333;
    }
    .stFileUploader {
        background-color: #ffffff;
    }
    h1 {
        color: #ff6347; 
        background-color: #e0e0e0; 
        padding: 10px;
        border-radius: 10px;
    }
    h2 {
        color: #32cd32; 
        background-color: #e0e0e0; 
        padding: 8px;
        border-radius: 8px;
    }
    h3 {
        color: #1e90ff;  
        background-color: #e0e0e0; 
        padding: 6px;
        border-radius: 6px;
    }
    h4, h5 { 
        color: #1e90ff;  
        background-color: #e0e0e0; 
        padding: 6px;
        border-radius: 6px;
    }
    .llm-response {
        color: #4b4b4b; 
        background-color: #e0e0e0; 
        padding: 10px;
        border-radius: 5px;
    }
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage and then keywords missing and last, final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(f"<div class='llm-response'>{response}</div>", unsafe_allow_html=True)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(f"<div class='llm-response'>{response}</div>", unsafe_allow_html=True)
    else:
        st.write("Please upload the resume")
