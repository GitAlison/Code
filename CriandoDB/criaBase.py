import sqlite3

conexao = sqlite3.connect("sistema.db")

cur = conexao.cursor()

cur.execute("""CREATE TABLE users(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                   user VARCHAR(20) NOT NULL,
                                   password VARCHAR(20) NOT NULL)
                """)

cur.close()
conexao.close()
print("CRIADO COM SUCESSO")