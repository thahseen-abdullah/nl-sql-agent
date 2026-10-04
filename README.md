# NL-SQL Agent

An end-to-end Natural Language to SQL application that allows users to ask questions about a PostgreSQL database using plain English.

The application uses an LLM to generate SQL from natural-language questions, validates the generated query, executes it against PostgreSQL, automatically corrects failed queries, and converts the results back into a natural-language answer.
## Live Demo

[NL-SQL Agent](https://nl-sql-agent-uvef3sw8cmhczhakxscvrk.streamlit.app/)

## Features

- Convert natural-language questions into PostgreSQL queries
- Dynamic PostgreSQL schema inspection
- SQL generation using the OpenAI API
- Read-only SQL validation
- Automatic SQL correction when query execution fails
- Natural-language interpretation of database results
- Display generated SQL alongside answers
- Read-only database explorer
- Interactive Streamlit web interface
- FastAPI backend
- PostgreSQL database with seeded e-commerce data
- Deployed multi-service architecture

## How It Works

The application follows an NL-to-SQL pipeline:

1. **Schema inspection** – The application reads the PostgreSQL database schema using `information_schema`.
2. **SQL generation** – The user's natural-language question and database schema are provided to the LLM to generate a PostgreSQL `SELECT` query.
3. **SQL validation** – The generated query is checked to ensure that only read-only SQL operations are allowed.
4. **Query execution** – The validated SQL query is executed against the PostgreSQL database.
5. **Error correction** – If the query fails, the database error is sent back to the LLM along with the original query and schema to generate a corrected query.
6. **Result interpretation** – The database results are provided to the LLM to generate a clear natural-language answer.
7. **Response** – The application displays the answer and the generated SQL query.

## Architecture

### Local Development

```text
Browser
  ↓
Streamlit
  ↓
FastAPI
  ↓
PostgreSQL
```

###Production

```text
Browser
  ↓
Streamlit Cloud
  ↓ HTTPS
FastAPI on Render
  ↓
PostgreSQL on Neon
  ↓
OpenAI API
```

## Tech Stack

- Python
- FastAPI
- Streamlit
- PostgreSQL
- OpenAI API
- psycopg
- Docker
- Render
- Neon

## Database

The application uses a PostgreSQL e-commerce database containing five tables:

- `customers`
- `products`
- `orders`
- `order_items`
- `payments`

The database is populated with sample customers, products, orders, order items, and payments.

## Example Questions

The agent can answer questions such as:

- Which customers are from Dubai?
- What products did Rahul Sharma buy?
- Which product has been ordered the most?
- How much money has each customer spent?
- How many completed orders were placed in September 2026?
- Which customer has spent the most money on completed orders?

## Project Structure

```text
nl-sql-agent/
│
├── app/
│   ├── agent.py
│   ├── api.py
│   ├── database.py
│   ├── database_viewer.py
│   ├── llm.py
│   ├── schema_inspector.py
│   ├── sql_executor.py
│   ├── sql_validator.py
│   └── ui.py
│
├── sql/
│   ├── schema.sql
│   └── seed.sql
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```
## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/thahseen-abdullah/nl-sql-agent.git
cd nl-sql-agent
```

### 2.Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3.Install dependencies

```bash
pip install -r requirements.txt
```

### 4.Configure environment variables

Create a .env file in the project root:
OPENAI_API_KEY=your_api_key
DATABASE_URL=your_database_url

For local development, the database URL should point to your local PostgreSQL instance.

### 5. Start PostgreSQL

The project uses PostgreSQL in Docker for local development.

Apply the database schema:

```bash
docker exec -i nl-sql-postgres psql -U nl_agent -d nl_sql_agent < sql/schema.sql
```

Load the sample data:

```bash
docker exec -i nl-sql-postgres psql -U nl_agent -d nl_sql_agent < sql/seed.sql
```

###6. Start the FastAPI backend

```bash
uvicorn app.api:app --reload
```

The API will run at:
http://127.0.0.1:8000

###7. Start the Streamlit frontend
Open another terminal and run:

```bash
python -m streamlit run app/ui.py
```


The application will open in your browser at the local Streamlit URL.

## How to Use

1. Open the application in your browser.
2. Enter a natural-language question about the database.
3. Click **Ask**.
4. View the generated answer.
5. Check the **Generated SQL** section to see the SQL query produced by the agent.
6. Use **Database Explorer** to inspect the available tables and data.

## Deployment

The application is deployed using separate services:

- **Streamlit Cloud** – Frontend
- **Render** – FastAPI backend
- **Neon** – Hosted PostgreSQL database
- **OpenAI API** – SQL generation, correction, and result interpretation

Environment variables and API credentials are configured through deployment platform secrets and are not committed to the repository.

## Limitations

This project is designed as a practical demonstration of an NL-to-SQL system rather than a production-grade database agent.

Current limitations include:

- SQL generation depends on LLM output.
- SQL validation uses keyword-based checks rather than a full SQL parser.
- Questions involving unavailable fields may not always be handled correctly.
- The application does not currently include authentication or user accounts.
- The database contains a relatively small sample dataset.
- The free Render deployment may experience cold starts.

## Future Improvements

Potential improvements include:

- Stronger SQL parsing and validation
- Query execution time limits
- Better handling of unavailable columns and ambiguous questions
- Conversation history
- Authentication
- Support for user-provided databases
- Query result visualizations
- More robust query planning and verification

## Author

**Thahseen Abdullah Bin Omer**

Built as a hands-on project to understand how natural-language interfaces can interact with relational databases using LLMs.