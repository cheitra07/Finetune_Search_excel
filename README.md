# Finetune_Search_excel
Excel data search using finetune,rag,bedrock
# 🧠 Machine Parts Repair Assistant (RAG + AWS Bedrock)

This GenAI app allows users to search for **machine part repair instructions** using a **Retrieval-Augmented Generation (RAG)** pipeline built with Excel data and deployed via **AWS Bedrock**.

## 💡 Features
- Searchable GenAI chatbot for machine parts
- Uses RAG (LangChain + Bedrock) on Excel-based repair data
- UI with Streamlit or Flask
- Deployable via AWS Lambda + API Gateway

## 🗃️ Data Format (Excel)
| Part Name | Issue Description | Repair Steps |
|-----------|-------------------|--------------|
| Gear Pump | Leakage           | Replace seals and clean inlet |

## 🚀 To Run Locally
```bash
pip install -r requirements.txt
streamlit run app/ui_streamlit.py
To Deploy on AWS

    Use deploy/lambda_handler.py for Lambda

    Connect Bedrock Titan or Claude using bedrock_config.py

---

## 🧱 Step-by-Step Code Support

I'll now begin with:

1. ✅ `requirements.txt`
2. ✅ `backend_rag.py` (LangChain + Bedrock code to read Excel and build RAG)
3. ✅ `ui_streamlit.py` (simple UI to ask and show answers)
4. ✅ `lambda_handler.py` (deploy backend to Lambda)

Let’s begin with the **first batch of files**.

---

### 📄 `requirements.txt`

```txt
pandas
openpyxl
streamlit
langchain
boto3
faiss-cpu
awscli
python-dotenv
