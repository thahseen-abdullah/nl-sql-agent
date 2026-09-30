import re


FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
]


def validate_sql(sql):
    sql = sql.strip()

    if not sql:
        return False

    first_word = sql.split()[0].upper()

    if first_word != "SELECT":
        return False

    for keyword in FORBIDDEN_KEYWORDS:
        pattern = rf"\b{keyword}\b"

        if re.search(pattern, sql, re.IGNORECASE):
            return False

    return True