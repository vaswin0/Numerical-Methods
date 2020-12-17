import numpy as np
import matplotlib.pyplot as plt

def rk4(f, t_init, y_init, delta, tt):
    
    t = np.arange(t_init,tt,delta)
    y = np.zeros(len(t))

    y[0] = y_init
    
    for i in range(len(y)-1):

        f1 = f(t[i],y[i])

        f2 = f(t[i] + (delta/2) , y[i] + (delta/2)*f1)

        f3 = f(t[i] + delta/2, y[i] + (delta/2)*f2)

        f4 =  f(t[i] + delta, y[i] + delta*f3)
        
        y[i+1] = y[i] + delta*(f1 + 2*f2 + 2*f3 +f4)/6


    return t,  y


f =  lambda t,y : y**t
t_init = 0
y_init = 1
delta = 0.001
tt = 1.75

t,y = rk4(f,t_init,y_init, delta, tt)

plt.plot(t,y)
plt.show()
