import math
from math import e
from numpy import log as ln
def secant_method_1(x0, x1, n): #this is in the form of x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    if n == 5:
        return
    func1 = e**x0-math.sin(x0)
    func2 = e**x1-math.sin(x1)
    ans = x1 - (func2)*((x1-x0)/((func2)-(func1)))
    sol = func1
    print(ans, end = ' ')
    print(sol)
    return secant_method_1(x1,ans,n+1)

def secant_method_2(x0, x1, n): #this is in the form of x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    if n == 5:
        return
    func1 = (x0-1)**3
    func2 = (x1-1)**3
    ans = x1 - (func2)*((x1-x0)/((func2)-(func1)))
    sol = func1
    print(ans, end = ' ')
    print(sol)
    return secant_method_2(x1,ans,n+1)

def secant_method_3(x0, x1, n): #this is in the form of x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    if n == 5:
        return
    func1 = (x0-1)**(1/3)
    func2 = (x1-1)**(1/3)
    ans = x1 - (func2)*((x1-x0)/((func2)-(func1)))
    sol = func1
    print(ans, end = ' ')
    print(sol)
    return secant_method_3(x1,ans,n+1)