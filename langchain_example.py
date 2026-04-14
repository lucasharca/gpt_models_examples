from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from pydantic import SecretStr

from config import api_key

url = "https://365datascience.com/courses/"

loader = WebBaseLoader(url)
raw_documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(raw_documents)

embeddings = OpenAIEmbeddings(
    api_key=SecretStr(api_key)
)

vectorstore = FAISS.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever()

llm = ChatOpenAI(
    api_key=SecretStr(api_key),
    model="gpt-4.1-mini",
    temperature=0
)

chat_history = []
query = "Which course on 365DataScience can help me learn AI?"

relevant_docs = retriever.invoke(query)

context = "\n\n".join(doc.page_content for doc in relevant_docs)

history_text = "\n".join(
    f"User: {q}\nAssistant: {a}" for q, a in chat_history
)

prompt = f"""
    Use the context below to answer the question.

    Conversation history:
    {history_text}
    Context: 
    {context}
    Question:
    {query}
"""

response = llm.invoke(prompt)
chat_history.append((query, response.content))

print(chat_history)