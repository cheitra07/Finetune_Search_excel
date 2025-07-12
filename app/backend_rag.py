import pandas as pd
from langchain.vectorstores import FAISS
from langchain.embeddings import BedrockEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.llms import Bedrock
import os

def load_excel_to_docs(excel_path):
    df = pd.read_excel(excel_path)
    docs = []

    for _, row in df.iterrows():
        content = f"Part: {row['Part Name']}\nIssue: {row['Issue Description']}\nRepair Steps: {row['Repair Steps']}"
        docs.append(Document(page_content=content))

    return docs

def create_vector_store(docs):
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(docs)

    embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1")  # or any Bedrock-supported model
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def run_query(vectorstore, query):
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(query)

    llm = Bedrock(model_id="anthropic.claude-v2")  # change as needed
    rag_prompt = "Use the following documents to answer the user's query.\n\n"

    context = "\n\n".join(doc.page_content for doc in docs)
    full_prompt = f"{rag_prompt}Context:\n{context}\n\nQuestion: {query}"

    return llm.invoke(full_prompt)
