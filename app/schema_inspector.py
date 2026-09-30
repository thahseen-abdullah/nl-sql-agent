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

def format_schema(columns):
    schema = {}

    for table_name, column_name, data_type in columns:
        if table_name not in schema:
            schema[table_name] = []

        schema[table_name].append(
            f"{column_name} ({data_type})"
        )

    return schema

def schema_to_text(schema):
    lines = []

    for table_name, columns in schema.items():
        lines.append(f"{table_name}:")

        for column in columns:
            lines.append(f"  {column}")

    return "\n".join(lines)