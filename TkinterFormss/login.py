from tkinter import *

class FormLogin:
    def __init__(self,top):
        self.Frame1 = Frame(top)
        self.Frame2 = Frame(top)

        self.Frame1.pack()
        self.Frame2.pack()

        #Botoes
        self.btnAcessar = Button(self.Frame1,text='Acessar',background='orange',width=10)
        self.btnCancelar = Button(self.Frame1,text='Cancelar',background='green',width=10)
        self.btnOutro = Button(self.Frame2,text='Outro',background ='blue')

        self.btnAcessar.pack(side=LEFT)
        self.btnCancelar.pack()
        self.btnOutro.pack()


raiz =Tk()
FormLogin(raiz)
raiz.mainloop()

