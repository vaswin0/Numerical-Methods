''' Newton-Raphson Method
Aswin
september 28 2020'''


import numpy as np #numerical python library
import sys



def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool'''
    return (abs(x-y) < 0.0000001)

def grad(f, x):
    h = 0.001
    return ((f(x + h) - f(x - h))/(2*h))
    #return (1 - 2*np.cos(x))

def NR_recur(fn,init):
    '''Recursive implementation
    of Fixed Point Iteration.
    Returns error if it doesnt 
    converge within the maximum
    recursive depth of python
    
    ARGS: function
    '''
    y = init - fn(init)/grad(fn, init)

    #print (y)
    
    
    if is_approx(y,init):
       
       print(y)
       

    else:
        
        NR_recur(fn,y)

    
    

def NR_iter(fn,num_iter, init_):
    '''Iterative implementation
    ARGS: function
          number of iteration
          init_-initial value
    Returns: y,root

    '''
    x = init_
    for i in range(num_iter):
        y = x - fn(x)/grad(fn, x)

        if is_approx(x,y):
            break

        else:
            x = y

    return y


print('***** root of  x - cos(2x) *****')
print('recursive') 
NR_recur(lambda x:x - 2*np.cos(x) ,1)
print('iterative')
print(NR_iter(lambda x:x - 2*np.cos(x) ,25,1))
print()

print('***** root of x**2 -3*x + 3 *****')
print('recursive')
NR_recur(lambda x:x**2 - 3*x +3 , 0.7j)
print('iterative')
print(NR_iter(lambda x:x**2 - 3*x +3 ,25,-0.7j))



   
