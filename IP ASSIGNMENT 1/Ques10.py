def fn(x):
    return x**3 - 10.5*x**2 + 34.5*x - 35

def df(x):
    return 3*x**2 - 21*x+34.5

inc=0

def func(poly, x0):
    global inc
    
    inc+=1
    if(inc>100):
        return False
    value = poly(x0)
    if(value==0):
        return x0
    m=df(x0)
    c=value-m*x0
    return func(poly, -c/m)

x0=float(input("Enter x0:"))
root=func(fn, x0)
if(x0):
    print('The root is :',round(root,3))
else:
    print('No root found')    


