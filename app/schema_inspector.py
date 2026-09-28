from app.database import get_connection


def get_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    tables = cursor.fetchall()

    connection.close()

    return tables


def get_columns():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            table_name,
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
    """)

    columns = cursor.fetchall()

    connection.close()

    return columns