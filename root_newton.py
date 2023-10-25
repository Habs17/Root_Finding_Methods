import math
from math import e
from numpy import log as ln
def newtons_method_1(x0,n): #this is in the form of x1 = x0 - f(x0)/f'(x0)
    if n == 5:
        return
    func = e**x0-math.sin(x0)
    deriv = e**x0-math.cos(x0)
    ans = x0 - (func)/(deriv)
    sol = func
    print(ans,end = ' ')
    print(sol)
    return newtons_method_1(ans,n+1)

def newtons_method_2(x0,n): #this is in the form of x1 = x0 - f(x0)/f'(x0)
    if n == 5:
        return
    func = (x0-1)**3
    deriv = 3*((x0-1)**2)
    ans = x0 - (func)/(deriv)
    sol = func
    print(ans,end = ' ')
    print(sol)
    return newtons_method_2(ans,n+1)

def newtons_method_3(x0,n): #this is in the form of x1 = x0 - f(x0)/f'(x0)
    if n == 5:
        return
    func = (x0-1)**(1/3)
    deriv = (1/3)*((x0-1)**(-2/3))
    ans = x0 - (func)/(deriv)
    sol = func
    print(ans,end = ' ')
    print(sol)
    return newtons_method_3(ans,n+1)