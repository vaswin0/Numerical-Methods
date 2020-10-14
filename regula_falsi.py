''' Regula Falsi 
Aswin
October 5  2020'''


import numpy as np



def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.000000000001)


    



def regula_falsi(f,num_iter, a, b):
    '''Iterative implementation
    ARGS: fn : function
          Num_iter : number of iteration
          a,b : initial interval
    Returns: c : root

    '''
    
    for i in range(num_iter):
        
        c  = (a*f(b) - b*f(a))/(f(b) - f(a)) # root of the secant line

        print('i =', i, 'a = ', a,'b = ', b , 'c = ', c)

        if is_approx(a,b):
            break

        else:
            if f(a)*f(c) > 0:
                a = c

            else:
                b = c

    return c




f =  lambda x : 25*x**4 - (x**2)/2 -2
root = regula_falsi(f, 100, 0.1, 1)
print('root = ', root,)
print('f(root) = ',f(root) )

print(' To reach the same accuracy,  regula falsi method takes almost  10x  more iterations than the secant method')
