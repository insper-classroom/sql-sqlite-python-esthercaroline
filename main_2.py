import sqlite3
from db.db_utils import *

def main():
    conn = sqlite3.connect('db/database_alunos.db')

    create_table(conn)

    students = [
        ("Ana Silva", "Computação", 2019),
        ("Pedro Silva", "Física", 2021),
        ("Carla Souza", "Computação", 2020),
        ("João Alves", "Matemática", 2018),
        ("Maria Oliveira", "Química", 2022)
    ]
    
    insert_students(conn, students)

    all_students = select_all_students(conn)
    print("Todos os estudantes:")
    print(all_students)

    conn.close()

