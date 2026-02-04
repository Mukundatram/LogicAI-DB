from app.db.connection import get_connection

FORBIDDEN = ["drop", "truncate", "alter"]

def run_sql(query: str):
    """
    Execute a MySQL SELECT query safely.
    """
    if any(word in query.lower() for word in FORBIDDEN):
        return {
            "sql": query,
            "rows": [],
            "error": "This operation is not allowed."
        }

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)

        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            return {
                "sql": query,
                "rows": rows,
                "error": None
            }
        else:
            conn.commit()
            return {
                "sql": query,
                "rows": [],
                "error": None
            }

    except Exception as e:
        return {
            "sql": query,
            "rows": [],
            "error": str(e)
        }

    finally:
        cursor.close()
        conn.close()
