import streamlit as st
import pandas as pd

from app.database import get_connection


TABLES = [
    "customers",
    "products",
    "orders",
    "order_items",
    "payments",
]


def get_table_data(table_name):
    connection = get_connection()

    query = f"SELECT * FROM {table_name};"

    dataframe = pd.read_sql(query, connection)

    connection.close()

    return dataframe


def show_database():
    st.title("Database Explorer")
    st.caption("Explore the data available to the NL-SQL Agent.")

    for table in TABLES:
        st.subheader(table)

        dataframe = get_table_data(table)

        st.dataframe(
            dataframe,
            use_container_width=True,
            hide_index=True
        )