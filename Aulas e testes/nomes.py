from tkinter import *
class Janela:
    def __init__(self,toplevel):
        self.frame=Frame(toplevel)
        self.frame.pack()
        self.b1=Button(self.frame)
        self.b1.bind("<Button-1>", self.press_b1)
        self.b1.bind("<ButtonRelease>", self.release_b1)
        self.b1['text'] = 'Clique em mim!'
        self.b1['width'], self.b1['bg'] = 20, 'brown'
        self.b1['fg']='yellow'
        self.b1.pack(side=LEFT)
        self.b2=Button(self.frame)
        self.b2['width'], self.b2['bg'] = 20, 'brown'
        self.b2['fg']='yellow'
        self.b2.pack(side=LEFT)
        self.b3=Button(self.frame, command=self.click_b3)
        self.b3['width'], self.b3['bg'] = 20, 'brown'
        self.b3['fg']='yellow'
        self.b3.pack(side=LEFT)
    def press_b1(self,event):
        self.b1['text']=''
        self.b2['text']='Errou! Estou aqui!'
    def release_b1(self,event):
        self.b2['text']=''
        self.b3['text']='OOOpa! Mudei de novo!'
    def click_b3(self):
        self.b3['text']='Ok... Você me pegou...'
instancia=Tk()
Janela(instancia)
instancia.mainloop()