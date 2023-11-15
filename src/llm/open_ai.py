from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import openai
from src.config.config import OPENAI_API_KEY, OPEN_AI_LLM_MODEL


openai.api_key = OPENAI_API_KEY


def process_prompt(prompt: str) -> str:
    chat = ChatOpenAI(
        model_name=OPEN_AI_LLM_MODEL,
        openai_api_key=openai.api_key,
        temperature=0,
        verbose=True,
    )
    response = chat([HumanMessage(content=prompt)])
    result = response.content
    return result
