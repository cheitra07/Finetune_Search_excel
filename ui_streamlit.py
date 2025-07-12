import streamlit as st
from app.backend_rag import load_excel_to_docs, create_vector_store, run_query

st.title("🔧 Machine Parts Repair Assistant")
query = st.text_input("Enter machine part or issue:")

if query:
    with st.spinner("Loading..."):
        docs = load_excel_to_docs("data/machine_parts.xlsx")
        vectorstore = create_vector_store(docs)
        response = run_query(vectorstore, query)

    st.markdown("### 🛠️ Repair Instructions")
    st.write(response)
