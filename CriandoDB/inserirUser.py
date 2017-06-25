import sqlite3

conexao = sqlite3.connect('sistema.db')
cur = conexao.cursor()

def user_inserir(user,password):
    return"""
    INSERT INTO users (user,password) VALUES('{}','{}')
    """.format(user,password)

print("DADOS INSERIDOR")


cur.execute(user_inserir('Joao','MariaQUIN'))
conexao.commit()
conexao.close()
