import json
import pandas as pd
from langchain.vectorstores import FAISS
from langchain.embeddings import BedrockEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.llms import Bedrock
from deploy.bedrock_config import get_bedrock_client

# You should store the Excel as a public S3 file or include a minimal copy locally in Lambda layer
EXCEL_FILE_PATH = "/tmp/machine_parts.xlsx"

def load_excel_to_docs():
    df = pd.read_excel(EXCEL_FILE_PATH)
    docs = []

    for _, row in df.iterrows():
        content = f"Part: {row['Part Name']}\nIssue: {row['Issue Description']}\nRepair Steps: {row['Repair Steps']}"
        docs.append(Document(page_content=content))
    return docs

def create_vector_store(docs):
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(docs)

    embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=get_bedrock_client())
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def run_query(vectorstore, query):
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(query)

    llm = Bedrock(model_id="anthropic.claude-v2", client=get_bedrock_client())
    context = "\n\n".join(doc.page_content for doc in docs)

    full_prompt = f"Use the following documents to answer the user's query.\n\nContext:\n{context}\n\nQuestion: {query}"
    return llm.invoke(full_prompt)

def lambda_handler(event, context):
    query = event.get("queryStringParameters", {}).get("query")

    if not query:
        return {"statusCode": 400, "body": json.dumps({"error": "Missing query parameter"})}

    docs = load_excel_to_docs()
    vectorstore = create_vector_store(docs)
    response = run_query(vectorstore, query)

    return {
        "statusCode": 200,
        "body": json.dumps({"response": response})
    }
