from tkinter import *
from tkinter import ttk


class Calculatrice:
    def __init__(self,root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title('Calculatrice')

        self.res = StringVar()
        self.valeur = ''
        self.boutons()



    def boutons(self):
        Entry(self.root, width=100, bg='orange', textvariable=self.res).place(x=50, y=10)

        # Button(self.root, text="+", command=lambda:self.affiche('+')).place(x=50,y=50)
        # Button(self.root, text="-", command=lambda: self.affiche('-')).place(x=50,y=100)
        # Button(self.root, text="x", command=lambda: self.affiche('x')).place(x=50,y=150)
        # Button(self.root, text="/", command=lambda: self.affiche('/')).place(x=50,y=200)
        # Button(self.root, text="^", command=lambda: self.affiche('^')).place(x=50,y=250)
        # Button(self.root, text="Root", command=lambda: self.affiche('Root')).place(x=50,y=300)


        tab = ['+','-', 'x', '/', '^', '(', ')']
        c=50
        for i in tab:
            Button(self.root, text=i, command=lambda a=i: self.affiche(a)).place(x=50, y=c)
            c+=50

        Button(self.root, text="+/-", command=lambda: self.changesigne()).place(x=50, y=500)


        for i in range(10):
            Button(self.root, text=str(i), command=lambda a=i: self.affiche(str(a))).place(x=300, y=i * 50 + 50)

        Button(self.root, text='=', command=lambda: self.resoudre()).place(x=500, y=50)
        Button(self.root, text='C', command=lambda: self.AC()).place(x=500, y=100)
        Button(self.root, text='Del', command=lambda: self.retour()).place(x=500, y=100)



    def resoudre(self):
        pass


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









    def somme(self, y):
            return (x + y)

    def substract(self, y):
            return (x - y)

    def multip(self, y):
            return (x * y)

    def divis(self, y):
            if y == 0:
                return ('error')
            else:
                return (x / y)

    def powerof(self, y):
            return (x ** y)

    def roots(self, y):
            if y == 0:
                return ('error')
            else:
                return (x ** (1 / y))


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
calculette = Calculatrice(root)




root.mainloop()

