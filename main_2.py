import sqlite3
from db.db_utils import *


conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()
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


update(conn, "Estudantes", "AnodeIngresso", "Nome", 2023, "Maria Oliveira")
all_students = select_all_students(conn)
conn.commit()
print(cursor.fetchall())

delete(conn, "Estudantes", "ID", 2)
all_students = select_all_students(conn)
conn.commit()
print(cursor.fetchall())

update(conn, "Estudantes", "AnodeIngresso", "Curso", 3018, "Computação")
all_students = select_all_students(conn)
conn.commit()
print(cursor.fetchall())

conn.close()
