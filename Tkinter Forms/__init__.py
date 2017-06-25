from tkinter import *

class formLogin:
    def __init__(self,toplevel):
        self.titulo = Frame(toplevel)
        self.titulo.pack()
        self.conteiner = Frame(toplevel)
        self.conteiner.pack(pady=5,padx=5)
        self.conteiner2 = Frame(toplevel)
        self.conteiner2.pack()
        self.conteiner3 = Frame(toplevel)
        self.conteiner3.pack()
        self.lbltitulo = Label(self.titulo,text='ACESSO AO SISTEMA',font='verdana 15').pack()

        self.lblNome= Label(self.conteiner,text='Usuario')
        self.lblPassword = Label(self.conteiner, text='Password')

        self.lblMessagem = Label(self.conteiner3, text='Aguardando dados')
        self.txtNome = Entry(self.conteiner)
        self.txtSenha = Entry(self.conteiner,show='§')

        self.btnAcessar = Button(self.conteiner2,text='ENTRAR',command=self.logar)
        self.btnCancelar = Button(self.conteiner2,text="CANCELAR",command=self.Sair)

        self.lblNome.grid(row=0)
        self.lblPassword.grid(row=1)


        self.txtNome.grid(row=0,column=1,pady=2)
        self.txtSenha.grid(row=1,column=1,pady=2)

        self.btnCancelar.pack(side=LEFT,padx=10)
        self.btnAcessar.pack(side=RIGHT,padx=10)
        self.lblMessagem.pack()

    def logar(self):
        nome = self.txtNome.get()
        senha = self.txtSenha.get()
        if nome =='alison' and senha =='123':
            self.lblMessagem['text'] = 'Logado Com sucesso'
            self.formSistema()
            self.Sair()

        else:
            self.lblMessagem['text'] = 'Error'
    def Sair(self):
        root.destroy()

    def formSistema(self):
        janela = Tk()
        janela.geometry("300x300+300+300")

root = Tk()

formLogin(root)
root.title('Login')
root.mainloop()