import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5433,
    dbname="nl_sql_agent",
    user="nl_agent",
    password="nl_agent_password"
)

cursor = connection.cursor()

cursor.execute("SELECT name FROM customers;")

result = cursor.fetchall()

print(result)

connection.close()