import streamlit as st
from summarizer_nltk import nltk_summarize

# Web app title
st.title("🧠 AI Text Summarizer (NLTK Version)")

# Text input area
text = st.text_area("Enter text to summarize:", height=200)

# Button to trigger summarization
if st.button("Summarize"):
    if text.strip():
        summary = nltk_summarize(text)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")