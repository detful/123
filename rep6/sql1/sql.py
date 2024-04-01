import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"database.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        start_date TEXT,
                                        end_date TEXT
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id INTEGER PRIMARY KEY,
                                    project_id INTEGER NOT NULL,
                                    name TEXT NOT NULL,
                                    description TEXT,
                                    status TEXT,
                                    start_date TEXT,
                                    end_date TEXT,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_tasks_table)
        print("Tables created successfully.")
    else:
        print("Error! cannot create the database connection.")

    if conn:
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()
