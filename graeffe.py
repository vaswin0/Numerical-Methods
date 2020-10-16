import numpy as np
p = [1,30/9,34/9,30/9, 25/9]




def pol(p, root):
    po =  0    
    n = len(p)

    for i in range(n):
        po +=  p[i]* root**(n-i-1)

    return po

def graeffe(p, num_iter):

    
    a =  []
    a = p
    

    for n in range(1,num_iter):
        

        roots = []
        b = np.square(a)

        for i in range(0,len(p)):
            for j in range(1, len(p)):
        
                if j%2 != 0:
            
                    if i-j < 0 or i+j  >= len(p):
                        b[i] += 0
                    else:
                        b[i] += -2*a[i-j]*a[i+j]
                
                else:
                    if i-j < 0 or i+j  >= len(p):
                        b[i] += 0
                    else:
    
                        b[i] += 2*a[i-j]*a[i+j]
            

        print('b =', b)
        print()

        a = b

    for i in range(1,len(b)):
          
        root  =  (b[i]/b[i-1])**(1/(2**n))

        roots.append(root)

        #print('roots =', roots)

        
        

    return roots

roots  = graeffe(p,7) 

print(roots)
print()


def Roots(roots):
    for i in range(len(roots)):
        
        

        if pol(p,-1*roots[i])  < pol(p,roots[i]):
            roots[i] = -1*roots[i]
    print(roots)
    roo =   roots[np.argmin([pol(p,root) for root in roots])]
    print(roo)




Roots(roots)





