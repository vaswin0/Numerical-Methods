''' 
Deuteron Potential well using
secant method
Aswin
October 5 2020
'''


import numpy as np #numerical python library




def is_approx(x,y):
    '''Function to check
    convergence
    ARGS: x,y
    RETURN: bool
    '''
    return (abs(x-y) < 0.000000000001)



    
    

def secant(f,num_iter, x0,x1,v0):
    '''Iterative implementation
    ARGS: function
          number of iteration
          init_ :initial value
    Returns: y,root

    '''
    if x0 > v0:
        print('E > V0')
        return
    for i in range(num_iter):
        
        
        x = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))
        print('i =', i, 'xn = ', x,'f(xn) = ', f(x))
        if is_approx(x,x1):
            break

        else:
            x0 = x1
            x1 = x


    return x


#in natural units

m = 0.938     #(GeV); reduced mass 
v0 = 0.02     #(GeV); depth of the potential well 
a = 2.1/0.197 #(GeV)^-1;width of the potential well  
h_ = 1        #h_bar  

f = lambda x:np.sqrt(2*m*(v0-abs(x)))*(1/np.tan(np.sqrt(2*m*a**2*abs(v0-x))/h_)) + np.sqrt(2*m*abs(x)) 
print()
root = secant(f ,10,0.001,0.011,v0)
if root != None:
    
    print()
    print('root = ',root,'MeV')
    print()
print('f(root) = ',f(root))

