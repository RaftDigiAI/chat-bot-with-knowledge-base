from typing import List
from langchain.docstore.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from src.config.config import OPENAI_API_KEY, VECTOR_STORE_FILE_PATH

from pandas import read_excel

documents: List[Document] = []
file_content = read_excel("./data.xlsx")

for row in file_content.iterrows():
    documents.append(
        Document(
            page_content=row[1]["content"],
            metadata={
                "source": row[1]["source"],
                "name": row[1]["name"],
                "price": row[1]["price"],
            },
        )
    )


db = FAISS.from_documents(documents, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))
db.save_local(VECTOR_STORE_FILE_PATH)
