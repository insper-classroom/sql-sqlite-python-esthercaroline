import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"



conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()
cursor.execute(""" DROP TABLE IF EXISTS Estudantes """)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
);
""")


alunos = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Silva", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
VALUES (?, ?, ?);
""", alunos)
conn.commit()

# Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive)
cursor.execute("SELECT * FROM Estudantes WHERE Ano_de_Ingresso BETWEEN 2019 AND 2020")
print("Estudantes que ingressaram entre 2019 e 2020:")
print(cursor.fetchall())

# Atualize o "Ano de Ingresso" de um estudante específico
novo_ano_ingresso = 2022
id_estudante_atualizar = 2  # Substitua pelo ID do estudante específico
cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE ID = ?", (novo_ano_ingresso, id_estudante_atualizar))
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

id_estudante_deletar = 4 
cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (id_estudante_deletar,))
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())


# Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019
cursor.execute("SELECT * FROM Estudantes WHERE Curso = 'Computação' AND Ano_de_Ingresso > 2019")
conn.commit()
print(cursor.fetchall())

# Altere os registros de ingresso dos alunos de Computação para 2018
cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = 2018 WHERE Curso = 'Computação'")
conn.commit()
cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

# Mostre todos os estudantes novamente
cursor.execute("SELECT * FROM Estudantes")
print("\nEstudantes após correção de registros de Computação:")
print(cursor.fetchall())

# Fecha a conexão com o banco de dados
conn.close()


