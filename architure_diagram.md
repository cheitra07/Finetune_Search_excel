[User]
   |
   ▼
[Streamlit UI or API Gateway]
   |
   ▼
[AWS Lambda Function]
   |
   ├── Load repair data (S3 Excel → /tmp/)
   ├── Embed with Titan (Bedrock Embeddings)
   ├── Search relevant docs (FAISS)
   └── Query Claude v2 → Response
   |
   ▼
[Return repair instructions]
