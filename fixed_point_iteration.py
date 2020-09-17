'''Fixed Point Iteration
Aswin
september 16 2020'''


import numpy as np #numerical python library
import sys



def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.0001)


def fpi_recur(fn,init):
    '''Recursive implementation
    of Fixed Point Iteration.
    Returns error if it doesnt 
    converge within the maximum
    recursive depth of python
    
    ARGS: function
    '''
    y = fn(init)
    
    
    if is_approx(y,init):
       
       print(y)
       

    else:
        
        fpi_recur(fn,y)

    
    

def fpi_iter(fn,num_iter, init_):
    '''Iterative implementation
    ARGS: function
          number of iteration
          init_-initial value
    Returns: y-fixed point

    '''
    x = init_
    for i in range(num_iter):
        y =  fn(x)

        if is_approx(x,y):
            break

        else:
            x = y

    return y


print('iterative:',fpi_iter(lambda x: np.exp(-2*x),100,0.7831))
print('recursive:')
fpi_recur(lambda x: np.exp(-2*x),0.5)



   
