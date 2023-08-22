import sqlite3

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudantes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Curso TEXT NOT NULL,
        Ano_de_Ingresso INTEGER
    );
    """)
    conn.commit()

def insert_students(conn, students):
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
    VALUES (?, ?, ?);
    """, students)
    conn.commit()

def select_all_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Estudantes")
    return cursor.fetchall()
