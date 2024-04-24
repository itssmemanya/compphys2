import numpy as np
import matplotlib.pyplot as plt
'''
u1′= u1 + 2u2 − 2u3 + e^−t
u2′= u2 + u3 − 2e^-t
u3′= u1 + 2u2 + e^-t
'''
def f(t,u):
    k=np.exp(-t)
    return [u[0]+2*u[1]-2*u[2]+k,u[1]+u[2]-2*k,u[0]+2*u[1]+k]

a=0
b=1
n=100
h=(b-a)/n
t=np.linspace(a,b,n+1)
iv=[3,-1,1] # initial values 
o=3  

def rk4(t,f):
    i=1
    u=np.zeros((n+1,o))
    u[0,:]=iv
    while i<=n:
        k1=f(t[i-1],u[i-1,:])
        k1[:]=[t*h*0.5 for t in k1]
        k2=f(t[i-1]+h/2,u[i-1,:]+k1)
        k2[:]=[t*h*0.5 for t in k2]
        k3=f(t[i-1]+h/2,u[i-1,:]+k2)
        k3[:]=[t*h for t in k3]
        k4=f(t[i-1]+h/2,u[i-1,:]+k3)
        k1[:]=[t/3 for t in k1]
        k2[:]=[t*2/3 for t in k2]
        k3[:]=[t/3 for t in k3]
        k4[:]=[t*h/6 for t in k4]
        u[i,:]=u[i-1,:]+k1+k2+k3+k4
        i+=1
    return u

y=rk4(t,f)
plt.plot(t,y[:,0], label='u1')
plt.plot(t,y[:,1], label='u2')
plt.plot(t,y[:,2], label='u3')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend()
plt.show()
