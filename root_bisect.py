import math
from math import e
from numpy import log as ln
def bisection_method_1(x0,x1,n):
    if n == 5:
        return
    fn = e**x0-math.sin(x0)
    fn1 = e**x1-math.sin(x1)
    c0 = (x0+x1)/2
    fnc0 = e**c0-math.sin(c0)
    sign = fn*fnc0
    if sign < 0:
        print(x0, ' ', c0)
        bisection_method_1(x0,c0,n+1)
    else:
        print(c0, ' ', x1)
        bisection_method_1(c0,x1,n+1)

def bisection_method_2(x0,x1,n):
    if n == 5:
        return
    fn = (x0-1)**3
    fn1 = (x1-1)**3
    c0 = (x0+x1)/2
    fnc0 = (c0-1)**3
    sign = fn*fnc0
    if sign < 0:
        print(x0, ' ', c0)
        bisection_method_2(x0,c0,n+1)
    else:
        print(c0, ' ', x1)
        bisection_method_2(c0,x1,n+1)

def bisection_method_3(x0,x1,n):
    if n == 5:
        return
    fn = (x0-1)**(1/3)
    fn1 = (x1-1)**(1/3)
    c0 = (x0+x1)/2
    fnc0 = (c0-1)**(1/3)
    sign = fn*fnc0
    if sign < 0:
        print(x0, ' ', c0)
        bisection_method_3(x0,c0,n+1)
    else:
        print(c0, ' ', x1)
        bisection_method_3(c0,x1,n+1)

