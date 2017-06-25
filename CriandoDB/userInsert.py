import sqlite3

conexao = sqlite3.connect('database.db')

cur = conexao.cursor()

def user_Insert(usuario,senha):
    return"""INSERT INTO usuarios(usuario,senha) VALUES('{}','{}')""".format(usuario,senha)
    print("INSERIDO COM SUCESSO")

def selectUser(usuario):
    return"SELECT  * FROM  usuarios WHERE usuario='{}'".format(usuario)

cur.execute('select * from usuarios')
#cur.execute(selectUser('THIAGO'))
#cur.execute(user_Insert('HUis','56892'))

for i in cur.fetchall():
    print(i)
cur.close()
conexao.commit()
conexao.close()