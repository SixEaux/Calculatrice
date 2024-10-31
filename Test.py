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

        Button(self.root, text="+", command=lambda:self.affiche('+')).place(x=50,y=50)
        Button(self.root, text="-", command=lambda: self.affiche('-')).place(x=50,y=100)
        Button(self.root, text="x", command=lambda: self.affiche('x')).place(x=50,y=150)
        Button(self.root, text="/", command=lambda: self.affiche('/')).place(x=50,y=200)
        Button(self.root, text="^", command=lambda: self.affiche('^')).place(x=50,y=250)
        Button(self.root, text="Root", command=lambda: self.affiche('Root')).place(x=50,y=300)

        Button(self.root, text="+/-", command=lambda: self.changesigne()).place(x=50, y=400)

        for i in range(10):
            Button(self.root, text=str(i), command=lambda a=i: self.affiche(str(a))).place(x=300, y=i * 50 + 50)


    def AC(self):
        self.valeur = ''
        self.res.set(self.valeur)

    def retour(self):
        self.valeur = self.valeur[:-1]
        self.res.set(self.valeur)

    def changesigne(self):
        self.valeur = '-' + self.valeur
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













# bouttext=Button(root, text="Afficher", command=choinomb)
# bouttext.pack(side=TOP, padx=50, pady=10)
#
# entry = Entry(root)
# entry.pack()
#
# frame = Frame(root)
# frame.pack()
# root.geometry("500x200")
#
# label = ttk.Label(frame, text=f"{int(x)}" )
# label.pack(side="left")
# label2 = ttk.Label(frame, text=f"{int(y)}")
# label2.pack(side="bottom")
#
# def on_button_click(operation):
#     if operation == "add":
#         result = somme(x, y)
#         res = Label(root, text=f"{int(result)}")
#         res.pack(side="bottom")
#         print(result)
#     elif operation == "sub":
#         result = substract(x, y)
#         res = Label(root, text=f"{int(result)}")
#         res.pack(side="right")
#         print(result)
#     elif operation == "mul":
#         result = multip(x, y)
#         res = Label(root, text=f"{int(result)}")
#         res.pack(side="bottom")
#         print(result)
#     elif operation == "div":
#         result = divis(x, y)
#         res = Label(root, text=f"{int(result)}")
#         res.pack(side="bottom")
#         print(result)
#     elif operation == "pow":
#         result = powerof(x, y)
#         res = Label(root, text=f"{int(result)}")
#         res.pack(side="bottom")
#         print(result)
#     elif operation == "root":
#         result = roots(x, y)
#         res = Label(root, text=f"{int(result)}")
#         res.pack(side="bottom")
#         print(result)



root=Tk()
calculette = Calculatrice(root)




root.mainloop()

