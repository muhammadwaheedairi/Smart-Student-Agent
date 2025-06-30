import streamlit as st
import asyncio
from main import ask_academic_question, provide_study_tips, summarize_text

st.set_page_config(page_title="🎓 Smart Student Agent", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center;'>🎓 Smart Student Agent</h1>
    <p style='text-align: center; color: gray;'>Ask, Learn, and Succeed — Powered by OpenAI Agent SDK + LiteLLM</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Navigation
feature = st.radio("Select Feature", ["📘 Academic Q&A", "🧠 Study Tips", "📝 Text Summary"])

# Event loop initializer
def run_async(func, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(func(*args))

# Feature 1: Academic Questions
if feature == "📘 Academic Q&A":
    question = st.text_area("Enter your academic question")
    if st.button("Get Answer"):
        if question.strip():
            with st.spinner("Thinking..."):
                answer = run_async(ask_academic_question, question)
            st.success(answer)
        else:
            st.warning("Please enter a valid academic question.")

# Feature 2: Study Tips
elif feature == "🧠 Study Tips":
    topic = st.text_input("Enter a topic you want to study better")
    if st.button("Get Study Tips"):
        if topic.strip():
            with st.spinner("Generating tips..."):
                tips = run_async(provide_study_tips, topic)
            st.info(tips)
        else:
            st.warning("Please enter a study topic.")

# Feature 3: Summarization
elif feature == "📝 Text Summary":
    passage = st.text_area("Paste the passage to summarize")
    if st.button("Summarize"):
        if passage.strip():
            with st.spinner("Summarizing..."):
                summary = run_async(summarize_text, passage)
            st.success(summary)
        else:
            st.warning("Please paste a passage for summarization.")
