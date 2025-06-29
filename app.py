import streamlit as st
from main import ask_academic_question, get_study_tips, summarize_text

st.set_page_config(page_title="Smart Student Agent", page_icon="📚")
st.title("🎓 Smart Student Agent (Powered by OpenRouter)")

tabs = st.tabs(["📚 Ask a Question", "🧠 Study Tips", "✂️ Summarize Text"])

# Tab 1: Academic Q&A
with tabs[0]:
    q = st.text_input("Ask your academic question:")
    if st.button("Get Answer"):
        with st.spinner("Thinking..."):
            st.success(ask_academic_question(q))

# Tab 2: Study Tips
with tabs[1]:
    topic = st.text_input("Enter a topic to get study tips:")
    if st.button("Get Study Tips"):
        with st.spinner("Gathering tips..."):
            st.info(get_study_tips(topic))

# Tab 3: Summarizer
with tabs[2]:
    text = st.text_area("Paste the text you want to summarize:")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            st.write(summarize_text(text))
