'''
Birge Vieta
Aswin
October 15  2020'''


import numpy as np #numerical python library




def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.000000000001)

def gradient(f, x):
    h = 0.0001
    return ((f(x + h) - f(x - h))/(2*h))
    



def birge_vieta(p,num_iter, init_):
    '''Iterative implementation
    ARGS: fn : function
          Num_iter : number of iteration
          init_ : initial value
    Returns: y : root

    '''
    x = init_
    for i in range(num_iter):
        b = p(x)
        c = gradient(p,x)
        y = x - b/c
        print('i =', i, 'x = ',x)
        if is_approx(x,y):
            break

        else:
            x = y

    return y




p = lambda x:x**4 + (30/9)*x**3 +(34/9)*x**2 + (30/9)*x + 25/9
root = birge_vieta(p, 100, 1)

print()

print('root = ', root)
print('p(root) = ',p(root) )
