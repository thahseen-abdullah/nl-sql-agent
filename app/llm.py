from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()


def ask_llm(prompt):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


def generate_sql(question, schema):
    prompt = f"""
You are a SQL generation assistant.

Convert the user's natural language question into a PostgreSQL SQL query.

Database schema:
{schema}

User question:
{question}

Rules:
- Only generate SELECT queries.
- Do not generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, or CREATE statements.
- Do not modify the database in any way.
- Return only the SQL query.
"""

    return ask_llm(prompt)

def correct_sql(question, schema, sql, error):
    prompt = f"""
You are a SQL correction assistant.

The previous SQL query failed when executed against PostgreSQL.

Database schema:
{schema}

User question:
{question}

Previous SQL:
{sql}

Database error:
{error}

Generate a corrected PostgreSQL SELECT query that answers the user's question.

Rules:
- Only generate SELECT queries.
- Do not generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, or CREATE statements.
- Return only the corrected SQL query.
"""

    return ask_llm(prompt)