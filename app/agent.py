from app.sql_executor import execute_query
from app.sql_validator import validate_sql
from app.schema_inspector import get_columns, format_schema, schema_to_text
from app.llm import generate_sql, correct_sql, interpret_results


def execute_generated_sql(sql):
    if not validate_sql(sql):
        raise ValueError("Generated SQL failed validation.")

    return execute_query(sql)


def ask_database(question):
    columns = get_columns()
    schema = format_schema(columns)
    schema_text = schema_to_text(schema)

    sql = generate_sql(question, schema_text)

    try:
        results = execute_generated_sql(sql)

    except Exception as error:
        print("First SQL attempt failed:")
        print(error)

        corrected_sql = correct_sql(
            question,
            schema_text,
            sql,
            error
        )

        print("\nCorrected SQL:")
        print(corrected_sql)

        results = execute_generated_sql(corrected_sql)
        sql = corrected_sql

    answer = interpret_results(question, results)

    return {
        "answer": answer,
        "sql": sql
    }