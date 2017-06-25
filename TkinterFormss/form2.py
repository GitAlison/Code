from tkinter import *


class Janela():
    def __init__(self, topLevel):

        self.conteiner1 = Frame(topLevel)
        self.conteiner1.pack()
        self.conteiner2 = Frame(topLevel)
        self.conteiner2.pack()
        # Botoes
        self.Botao = Button(self.conteiner2, text='Mudar Cor', background='green', width=15, font=20,
                            foreground='white')
        self.Botao.pack(side=LEFT)
        self.Botao.bind("<Button-1>", self.muda_cor)
        # Labels
        self.Texto = Label(self.conteiner1, text='Clique Aqui !', font=20)
        self.Texto.pack(side=TOP)

    def muda_cor(self,event):

        if self.Botao['bg'] == 'green':
            self.Botao['bg'] = 'yellow'
            self.Texto['text'] = 'Clique para ficar verde'
        else:
            self.Botao['bg'] = 'green'
            self.Texto['text'] = 'Clique para ficar amarelo'


raiz = Tk()
Janela(raiz)
raiz.mainloop()
