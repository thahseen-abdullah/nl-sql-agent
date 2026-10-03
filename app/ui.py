import streamlit as st
import requests
from app.database_viewer import show_database

from app.schema_inspector import get_columns, format_schema


st.title("NL-SQL Agent")
st.caption("Built by Thahseen Abdullah Bin Omer")

st.write("Ask questions about the database using natural language.")


question = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

    result = response.json()

    if response.status_code == 200:
        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Generated SQL")
        st.code(result["sql"], language="sql")

    else:
        st.error(result["detail"])

st.divider()

if st.button("📊 View Database"):
    show_database()