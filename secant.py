''' 
secant Method
Aswin
October 5 2020
'''


import numpy as np #numerical python library
import sys



def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.000000000001)



    
    

def secant(f,num_iter, x0,x1):
    '''Iterative implementation
    ARGS: function
          number of iteration
          init_-initial value
    Returns: y,root

    '''
    
    for i in range(num_iter):
        
        
        x = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))
        print('i =', i, 'xn = ', x,'f(xn) = ', f(x))
        if is_approx(x,x1):
            break

        else:
            x0 = x1
            x1 = x


    return x


f = lambda x:25*x**4 - x**2/2 -2 
print()
root = secant(f ,10000,1,2)
print()
print('root = ',root)
print()
print('f(root) = ',f(root))

