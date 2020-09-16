'''Fixed Point Iteration
Aswin
september 16 2020'''


import numpy as np #numerical python library


def f(x):
    
    return np.exp(-2*x)

def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.0001)


def fpa(fn,init):
    '''Recursive implementation
    of FIxed Point Iteration
    ARGS: function
    '''
    y = fn(init)
    
    
    if is_approx(y,init):
       
       print(y)
       

    else:
        
        fpa(fn,y)

    
    

fpa(f,0.731689)




