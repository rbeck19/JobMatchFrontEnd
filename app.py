from rake_nltk import Rake
from keybert import KeyBERT
import streamlit as st
import re
from pdfminer.high_level import extract_text

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
stopWords = stopwords.words('english')
LEMMATIZER = WordNetLemmatizer()

# ----------- Functions -------------


def normalized_text(text: str):
    text = text.lower()
    text = text.strip()
    text = re.sub('[^\w\s]', '', text)
    text = text.split()
    text = [word for word in text if word.isalpha()]
    text = [word for word in text if word not in stopWords and len(word) >= 2]
    text = [LEMMATIZER.lemmatize(word) for word in text]
    return ' '.join(map(str, text))


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


def extract_name_from_resume(text):
    name = None
    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()
    return name


def extract_skills_from_resume(text, skills_list):
    skills = []
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)
    return skills


# --------------- Stream-lit Display -----------

st.title("Milky Way Matchmaking")
uploaded_file = st.file_uploader("Upload your resume here")


skills_list = ['Python', 'Data Analysis', 'Machine Learning',
               'Communication', 'Project Management', 'Deep Learning', 'SQL', 'Tableau']


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
    pdfname = extract_name_from_resume(pdftext)
    st.text(pdfname)

text_input = st.text_input(
    "Enter Job Description",
    placeholder='',
)

if text_input:
    # st.write("You entered: ", text_input)
    # kw_model = KeyBERT()
    # keywords = kw_model.extract_keywords(text_input)
    # print(keywords)
    #
    normText = normalized_text(text_input)
    print(normText)
    # rake_nltk_var = Rake()
    # rake_nltk_var.extract_keywords_from_text(text_input)
    # keyword_extracted = rake_nltk_var.get_ranked_phrases()
    # print(keyword_extracted)
    r = Rake()
    a = r.extract_keywords_from_text(text_input)
    b = r.get_ranked_phrases()
    c = r.get_ranked_phrases_with_scores()
    # e = r.extract_keywords_from_sentences(normText)
    # print(b)
    print(c)
    # print(e)
