import numpy as np
import matplotlib.pyplot as plt

#dx/dt=1/(x^2+t^2)
#Defining variable u=t/(t+1), t=u/(1-u)
#dx/du=1/(x^2(1-u)^2+u^2)
def f(u,x):
    return 1/((x**2)*((1-u)**2)+u**2)

def tf(u):
    return u/(1-u)

a=0
b=0.999
n=100
h=(b-a)/n
u=np.linspace(a,b,n+1)
iv=1 # initial values for y and y'
o=1  # order

def rk4(t,f):
    i=1
    y=np.zeros((n+1,o))
    y[0]=iv
    while i<=n:
        k1=h*f(t[i-1],y[i-1])
        k2=h*f(t[i-1]+h/2,y[i-1]+k1/2)
        k3=h*f(t[i-1]+h/2,y[i-1]+k2/2)
        k4=h*f(t[i-1]+h/2,y[i-1]+k3)
        y[i]=y[i-1]+k1/6+k2/3+k3/3+k4/6  
        i+=1
    return y

x=rk4(u,f)
t=tf(u)
plt.plot(t,x, label='f by RK4 Method')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()
