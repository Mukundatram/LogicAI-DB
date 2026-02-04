from app.db.connection import get_connection

def load_schema() -> str:
    """
    Reads MySQL schema for the current database
    and returns a human-readable schema description.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = DATABASE()
        ORDER BY TABLE_NAME, ORDINAL_POSITION
    """)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    schema = {}
    for row in rows:
        table = row["TABLE_NAME"]
        column = row["COLUMN_NAME"]
        dtype = row["DATA_TYPE"]

        schema.setdefault(table, []).append(f"- {column} ({dtype})")

    schema_text = "DATABASE SCHEMA:\n\n"
    for table, columns in schema.items():
        schema_text += f"Table {table}:\n"
        schema_text += "\n".join(columns) + "\n\n"

    return schema_text
