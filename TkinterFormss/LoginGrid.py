from tkinter import *

class formLogin:
	def __init__ (self,toplevel):

		self.conteiner = Frame(toplevel)
		self.conteiner.pack()
		
		self.lblUser = Label(self.conteiner, text='USUARIO').grid(row=0)
		self.lblPassword = Label(self.conteiner,text='PASSWORD').grid(row=1)

		self.entry = Entry(self.conteiner).grid(row=0,column=1)
		self.entry2 = Entry(self.conteiner).grid(row=1,column=1)
		
		self.botao1 = Button(self.conteiner, text='logar').grid(row=2,column=0)
		self.botao2 = Button(self.conteiner, text='Cancelar').grid(row=2,column=1)
	
		

root = Tk()

formLogin(root)

root.mainloop()
