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
