from tkinter import *
from tkinter import ttk
import random

class Calculatrice:
    def __init__(self,root, p=False):
        self.root = root
        self.root.geometry('600x600')
        self.root.title('Calculatrice')
        self.p=p
        self.res = StringVar()
        self.valeur = ''
        self.boutons()



    def boutons(self):
        Entry(self.root, width=100, bg='orange', textvariable=self.res).place(x=0, y=20)


        tab = ['+','-', 'x', '/', '^', '(', ')']
        c=50
        for i in tab:
            Button(self.root, text=i, command=lambda a=i: self.affiche(a), width= 10, height=3).place(x=50, y=c)
            c+=50


        if not self.p:
            for i in range(10):
                Button(self.root, text=str(i), command=lambda a=i: self.affiche(str(a)),height=3,width=10).place(x=300, y=i * 50 + 50)

        elif self.p:
            t=[str(i) for i in range(10)]
            for i in range(10):
                a=random.choice(t)
                Button(self.root, text=a, command=lambda h=a: self.affiche(h)).place(x=300, y=i * 50 + 50)
                t.remove(a)

        Button(self.root, text='=', command=lambda: self.calculate_expression(), width= 10, height=3).place(x=500, y=50)
        Button(self.root, text='C', command=lambda: self.AC(), width= 10,height=3).place(x=500, y=150)
        Button(self.root, text='Del', command=lambda: self.retour(), width= 10, height=3).place(x=500, y=100)





    def AC(self):
        self.valeur = ''
        self.res.set(self.valeur)

    def retour(self):
        self.valeur = self.valeur[:-1]
        self.res.set(self.valeur)

    def changesigne(self):
        self.valeur = '-' + '(' + self.valeur + ')'
        self.res.set(self.valeur)

    def affiche(self,valeur):
        self.valeur += str(valeur)
        self.res.set(self.valeur)



    def calculate_expression(self):
            expr = self.valeur.replace('x', '*').replace('^', '**')
            try:
                result = eval(expr)
                self.res.set(result)
                self.valeur = str(result)
            except (SyntaxError, ZeroDivisionError):
                self.res.set("Error")
                self.valeur = ""





root=Tk()
calculette = Calculatrice(root,False)


root.mainloop()

