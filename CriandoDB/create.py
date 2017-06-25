import sqlite3

conexao = sqlite3.connect('database.db')

cur = conexao.cursor()

cur.execute('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario VARCHAR(20) NOT NULL,
                senha VARCHAR(20) NOT NULL)''')

cur.close()
conexao.close()