from multiprocessing.util import sub_debug
from tkinter import *
from tkinter import ttk

x=float(input("Enter the value of x: "))
y=float(input("Enter the value of y: "))


def somme(x,y):
    return(x+y)
def substract(x,y):
    return(x-y)
def multip(x,y):
    return(x*y)
def divis(x,y):
    if y==0:
        return('error')
    else:
        return(x/y)
def powerof(x,y):
    return(x**y)
def roots(x,y):
    if y==0:
        return('error')
    else:
        return(x**(1/y))


root = Tk()

frame = Frame(root)
frame.pack()
root.geometry("500x200")

label = ttk.Label(frame, text=f"{int(x)}" )
label.pack(side="left")
label2 = ttk.Label(frame, text=f"{int(y)}")
label2.pack(side="bottom")

def on_button_click(operation):
    if operation == "add":
        result = somme(x, y)
    elif operation == "sub":
        result = substract(x, y)
    elif operation == "mul":
        result = multip(x, y)
    elif operation == "div":
        result = divis(x, y)
    elif operation == "pow":
        result = powerof(x, y)
    elif operation == "root":
        result = roots(x, y)

button_add = Button(root, text="Add (+)", command=lambda: on_button_click("add"))
button_sub = Button(root, text="Subtract (-)", command=lambda: on_button_click("sub"))
button_mul = Button(root, text="Multiply (*)", command=lambda: on_button_click("mul"))
button_div = Button(root, text="Divide (/)", command=lambda: on_button_click("div"))
button_pow = Button(root, text="Power (^)", command=lambda: on_button_click("pow"))
button_root = Button(root, text="Root", command=lambda: on_button_click("root"))

button_add.pack(padx=10, pady=5)
button_sub.pack(padx=10, pady=5)
button_mul.pack(padx=10, pady=5)
button_div.pack(padx=10, pady=5)
button_pow.pack(padx=10, pady=5)
button_root.pack(padx=10, pady=5)

root.mainloop()

