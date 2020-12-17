import numpy as np
import matplotlib.pyplot as plt


def rk2(f, t_init, y_init, delta, tt):
    
    t = np.arange(t_init,tt,delta)
    y = np.zeros(len(t))

    y[0] = y_init
    
    for i in range(len(y)-1):
        
        y[i+1] = y[i] + delta*f(t[i] + delta/2 , y[i] + (delta/2)*f(t[i], y[i]))


    return t,  y


f =  lambda t,y : t*y
t_init = -10
y_init = 100
delta = 0.0001
tt = 10

t,y = rk2(f,t_init,y_init, delta, tt)

plt.plot(t,y)
plt.show()
