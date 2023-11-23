import os

from dotenv import load_dotenv

load_dotenv()


OPEN_AI_LLM_MODEL = os.getenv("OPEN_AI_LLM_MODEL", "gpt-3.5-turbo")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
VECTOR_STORE_FILE_PATH = os.getenv("VECTOR_STORE_FILE_PATH", "index")
