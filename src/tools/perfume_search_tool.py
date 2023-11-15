from langchain.vectorstores import FAISS

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from pydantic import BaseModel

from src.config.config import OPEN_AI_LLM_MODEL, OPENAI_API_KEY, VECTOR_STORE_FILE_PATH

llm = ChatOpenAI(
    temperature=0.0, model=OPEN_AI_LLM_MODEL, openai_api_key=OPENAI_API_KEY
)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vector_store = FAISS.load_local(VECTOR_STORE_FILE_PATH, embeddings)


PERFUME_TOOL_DESCRIPTION = """Useful for finding a perfume by name, brand, or fragrance notes.
    Information in database is in Russian.
    Action: search for a perfume by name, brand, or fragrance notes.
    Action Input: name, brand, or fragrance notes
    Action Output: perfume data with url and name
    """


class PerfumeSearchTool(BaseModel):
    name: str = "perfume_search"
    description: str = PERFUME_TOOL_DESCRIPTION

    @staticmethod
    def run(input: str):
        retrieval_qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(),
            return_source_documents=True,
        )
        result = retrieval_qa({"query": input})
        answer = result["result"]
        docs = result["source_documents"]
        answer = answer + "\n---"
        for doc in docs:
            answer = answer + "\n" + doc.metadata["name"] + "-" + doc.metadata["source"]
        answer = answer + "\n---"
        return answer
