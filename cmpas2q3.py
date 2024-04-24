import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return [y[1],2*y[1]-y[0]+x*np.exp(x)-x]
def sol(x):
    return (-12+12*np.exp(x)-6*x-6*x*np.exp(x)+np.exp(x)*(x**3))/6
#Screenshot 2024-04-10 175620
a=0
b=1
n=100
h=(b-a)/n
x=np.linspace(a,b,n+1)
iv=[0,0] # initial values for y and y'
o=2  # order

def rk4(a,b,h,n,x,iv,o,f):
    i=1
    y=np.zeros((n+1,o))
    y[0,:]=iv
    while i<=n:
        k1=f(x[i-1],y[i-1,:])
        k1[:]=[x*h*0.5 for x in k1]
        k2=f(x[i-1]+h/2,y[i-1,:]+k1)
        k2[:]=[x*h*0.5 for x in k2]
        k3=f(x[i-1]+h/2,y[i-1,:]+k2)
        k3[:]=[x*h for x in k3]
        k4=f(x[i-1]+h/2,y[i-1,:]+k3)
        k1[:]=[x/3 for x in k1]
        k2[:]=[x*2/3 for x in k2]
        k3[:]=[x/3 for x in k3]
        k4[:]=[x*h/6 for x in k4]
        y[i,:]=y[i-1,:]+k1+k2+k3+k4
        i+=1
    return y

y=rk4(a,b,h,n,x,iv,o,f)
ysol=sol(x)
plt.plot(x,y[:,0], label='f by RK4 Method')
plt.plot(x,ysol, label='Analytical solution',linestyle=':',linewidth=4)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
