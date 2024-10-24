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



import tkinter as tk


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

    # Display the result in the terminal
    print(result)


# Input values
x = float(input('Give x: '))
y = float(input('Give y: '))

# Create the main window
root = tk.Tk()

# Create buttons for each operation
button_add = tk.Button(root, text="Add (+)", command=lambda: on_button_click("add"))
button_sub = tk.Button(root, text="Subtract (-)", command=lambda: on_button_click("sub"))
button_mul = tk.Button(root, text="Multiply (*)", command=lambda: on_button_click("mul"))
button_div = tk.Button(root, text="Divide (/)", command=lambda: on_button_click("div"))
button_pow = tk.Button(root, text="Power (^)", command=lambda: on_button_click("pow"))
button_root = tk.Button(root, text="Root", command=lambda: on_button_click("root"))

# Arrange buttons in the window using pack or grid
button_add.pack(padx=10, pady=5)
button_sub.pack(padx=10, pady=5)
button_mul.pack(padx=10, pady=5)
button_div.pack(padx=10, pady=5)
button_pow.pack(padx=10, pady=5)
button_root.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()