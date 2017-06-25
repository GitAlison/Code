arquivo= open("Novo.txt","w")

for linha in range(1,100):
    arquivo.write("\n[{:2}]".format(linha))
arquivo.close()
