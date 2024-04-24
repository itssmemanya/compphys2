import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return y/t-(y/t)**2

def sol(t):
    return t/(1+np.log(t))

a=1
b=2
h=0.1
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
iv=1

def euler(a,b,h,n,t,iv,f):
    i=1
    y=np.linspace(a,b,n+1)
    abserr=np.zeros(n+1)
    relerr=np.zeros(n+1)
    y[0]=iv
    while i<=n:
        y[i]=y[i-1]+h*f(t[i-1],y[i-1])
        abserr[i]=np.absolute(y[i]-sol(t[i]))
        relerr[i]=abserr[i]/sol(t[i])
        i+=1
    return y,abserr,relerr

ye,abserr,relerr=euler(a,b,h,n,t,iv,f)
ysol=sol(t)

plt.subplot(1,2,1)
plt.plot(t,ye, label='f by Euler Method')
plt.plot(t,ysol, label='Analytical solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.grid(True)
plt.subplot(1,2,2)
plt.plot(t,abserr, label='Absolute Error by Euler Method')
plt.plot(t,relerr, label='Relative Error by Euler Method')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

