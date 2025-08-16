from agents import (
    AsyncOpenAI, # or from openai import AsyncOpenAI 
    OpenAIChatCompletionsModel,    
    RunConfig
)
import os
from dotenv import load_dotenv

# api_key and base url
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure that it is defined in your .env file.")

# client
gemini_client = AsyncOpenAI(api_key=api_key, base_url=base_url)

# model
GEMINI_MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)

# runconfig
run_config = RunConfig(
    model=GEMINI_MODEL,
    tracing_disabled=True,
)

