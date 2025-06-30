import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI

# 🔐 Load API key from .env
load_dotenv()
api_key = os.getenv("LITELLM_API_KEY")

# ✅ LiteLLM-compatible OpenRouter base URL
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1/"
)

# 🧠 Define Agent
student_agent = Agent(
    name="Smart Student Agent",
    instructions=(
        "You are a helpful study assistant that can:\n"
        "- Answer academic questions\n"
        "- Provide effective study tips\n"
        "- Summarize short passages clearly\n"
        "Always reply in a simple and clear tone."
    ),
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-r1-0528:free",  # ✅ Change to valid OpenRouter model
        openai_client=client
    )
)

# 📚 Academic Q&A
async def ask_academic_question(query: str) -> str:
    result = await Runner.run(student_agent, query)
    return result.final_output

# 📖 Study Tips
async def provide_study_tips(topic: str) -> str:
    prompt = f"Give me 5 simple study tips for the topic: {topic}"
    result = await Runner.run(student_agent, prompt)
    return result.final_output

# ✂️ Summarizer
async def summarize_text(text: str) -> str:
    prompt = f"Summarize this in 3 lines:\n{text}"
    result = await Runner.run(student_agent, prompt)
    return result.final_output
