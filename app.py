import streamlit as st
import re
from pdfminer.high_level import extract_text

st.title("Milky Way Matchmaking")
uploaded_file = st.file_uploader("Upload your resume here")


def extract_text_from_pdf(file):
    return extract_text(file)


def extract_contact_number_from_resume(text):
    contact_number = None
    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()
    return contact_number


def extract_email_from_resume(text):
    email = None
    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    return email


skills_list = ['Python', 'Data Analysis', 'Machine Learning',
               'Communication', 'Project Management', 'Deep Learning', 'SQL', 'Tableau']


def extract_skills_from_resume(text, skills_list):
    skills = []
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)
    return skills


if uploaded_file:
    st.text("We have your Resume")
    pdftext = extract_text_from_pdf(uploaded_file)
    # st.text(pdftext)
    pdfcontact = extract_contact_number_from_resume(pdftext)
    st.text(pdfcontact)
    pdfemail = extract_email_from_resume(pdftext)
    st.text(pdfemail)
    pdfskills = extract_skills_from_resume(pdftext, skills_list)
    st.text(pdfskills)
