import os

from dotenv import load_dotenv

load_dotenv()


OPEN_AI_LLM_MODEL = os.getenv("OPEN_AI_LLM_MODEL", "gpt-3.5-turbo")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
WEVIATE_URL = os.getenv("WEVIATE_URL", "http://localhost:8080")
