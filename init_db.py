import sqlite3
from pathlib import Path

DB_PATH = Path("database.db")
SQL_DIR = Path("sql")


def execute_sql_file(connection: sqlite3.Connection, file_path: Path) -> None:
    script = file_path.read_text(encoding="utf-8")
    connection.executescript(script)


def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    execute_sql_file(conn, SQL_DIR / "01_create_tables.sql")
    execute_sql_file(conn, SQL_DIR / "02_insert_data.sql")

    conn.commit()
    conn.close()
    print("База данных успешно создана: database.db")


if __name__ == "__main__":
    main()
