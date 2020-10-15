''' Deuteron potential well
using Newton-Raphson
Aswin
October 5  2020'''


import numpy as np #numerical python library
import sys



def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.000000000001)

def gradient(f, x):
    h = 0.0001
    return ((f(x + h) - f(x - h))/(2*h))
    



def NR_iter(fn,num_iter, init_,v0):
    '''Iterative implementation
    ARGS: fn : function
          Num_iter : number of iteration
          init_ : initial value
    Returns: y : root

    '''
    if init_ > v0:
        print('E > V0')
        return
    x = init_
    for i in range(num_iter):
        
        y = x - fn(x)/gradient(f,x)
        print('i =', i, 'xn = ', y,'f(xn) = ', fn(y))
        if is_approx(x,y):
            break

        else:
            x = y

    return y

#in natural units
m = 0.938     #(GeV); reduced mass
v0 = 0.02     #(GeV); depth of the potential well
a = 2.1/0.197 #(GeV)^-1;width of the potential well
h_ = 1        #h_bar 


f = lambda x:np.sqrt(2*m*(v0-abs(x)))*(1/np.tan(np.sqrt(2*m*a**2*abs(v0-x))/h_)) + np.sqrt(2*m*abs(x))
root = NR_iter(f, 20, 0.011,v0)
print()
if root != None:
    print('root = ', root,'MeV')
    print('f(root) = ',f(root) )
