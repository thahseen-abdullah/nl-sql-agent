from app.database import get_connection


def execute_query(sql):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(sql)

    results = cursor.fetchall()

    connection.close()

    return results