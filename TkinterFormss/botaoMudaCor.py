from tkinter import *

class formLogin:
    def __init__(self,top):
        self.Conteiner = Frame(top)
        self.Conteiner1 = Frame(top)
        self.Conteiner2 = Frame(top)
        self.Conteiner3 = Frame(top)
        self.Conteiner.pack()
        self.Conteiner1.pack()
        self.Conteiner2.pack()
        self.Conteiner3.pack()


        #Labels

        self.lblTitulo = Label(self.Conteiner,text='Acesso ao sistema',font=15,foreground='blue')
        self.lblUser = Label(self.Conteiner1,text='User:')
        self.lblPassword = Label(self.Conteiner2, text='Password:')
        #Entry
        self.txtUser = Entry(self.Conteiner1,width=10)
        self.txtPassword = Entry(self.Conteiner2, width=10)

        #Button
        self.bntAcessar = Button(self.Conteiner3,text='Acessar',width=10)
        self.bntCancelar = Button(self.Conteiner3, text='Cancelar', width=10)

        self.bntCancelar.pack(side=LEFT,pady=10,padx=10)
        self.bntAcessar.pack(side=RIGHT,pady=10,padx=10)
        self.lblPassword.pack(side=LEFT)
        self.lblUser.pack(side=LEFT)
        self.lblTitulo.pack()
        self.txtUser.pack(side=RIGHT)
        self.txtPassword.pack(side=RIGHT)

raiz =Tk()
formLogin(raiz)
raiz.mainloop()
























'''from tkinter import *

class FormBotao:

    def __init__(self, topLevel):

        self.Conteiner1 = Frame(topLevel)
        self.Conteiner2 = Frame(topLevel)
        self.Conteiner1.pack()
        self.Conteiner2.pack()

        #Buttons
        self.Texto = Label(self.Conteiner1,text='Clique para ficar amarelo')
        self.Botao = Button(self.Conteiner2,text='Clique aqui',background='green',width=15)
        self.Botao1 = Button(self.Conteiner2,text="ALMENTAR")

        self.Texto.pack()
        self.Botao.pack()
        self.Botao1.pack()
        #event
        self.Botao.bind("<Motion>", self.muda_cor)
        self.Botao1.bind("<Motion>",self.Almentar)


    def Almentar(self,event):
        self.Botao['width']+=1



    def muda_cor(self,event):
        if self.Botao['bg'] =='green':
            self.Botao['bg']='yellow'
            self.Texto['text']='CLIQUE PARA FICAR VERDE'
        else:
            self.Botao['bg'] = 'green'
            self.Texto['text']='CLIQUE PARA FICAR AMARELO'



raiz = Tk()
FormBotao(raiz)
raiz.title("MUDAR COR DO BOTAO")
raiz.mainloop()
'''