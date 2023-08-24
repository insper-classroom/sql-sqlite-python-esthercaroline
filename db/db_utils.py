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

def insert_students(conn, estudantes):
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
    VALUES (?, ?, ?);
    """, estudantes)
    conn.commit()

def select_all_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Estudantes")
    return cursor.fetchall()

def update(conn, tabela, atualizar, identificador, novo, nome_iden):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {tabela} SET {atualizar} = ? WHERE {identificador} = ?", (novo, nome_iden))
    conn.commit()

def delete(conn, tabela, identificador, nome_deletar):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (nome_deletar,))
    conn.commit()
