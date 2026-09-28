import psycopg


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5433,
        dbname="nl_sql_agent",
        user="nl_agent",
        password="nl_agent_password"
    )

    return connection