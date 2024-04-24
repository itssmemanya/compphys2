# Algorithm
# g(y[n+1])=y[n+1]-hf(t[n+1],y[n+1])-y[n]=0
# Use Newton Raphson to find y[n+1]
import numpy as np
import scipy.optimize as roots
import matplotlib.pyplot as plt

def f1(x,y):
    return -9*y

def f2(x,y):
    return -20*(y-x)**2+2*x

a1=0
b1=1
n1=100
h1=(b1-a1)/(n1)
x1=np.linspace(a1,b1,n1+1)
iv1=np.e

a2=0
b2=1
n2=100
h2=(b2-a2)/n2
x2=np.linspace(a2,b2,n2+1)
iv2=1/3

def backeuler(a,b,h,n,x,iv,f):
    i=1
    y=np.linspace(a,b,n+1)
    y[0]=iv
    while i<=n:
        def backf(yn):
            return yn-h*f(x[i],yn)-y[i-1]
        y[i]=roots.newton(backf,0)
        i+=1
    return y

y1=backeuler(a1,b1,h1,n1,x1,iv1,f1)
y2=backeuler(a2,b2,h2,n2,x2,iv2,f2)

plt.plot(x1,y1, label='f1 by Backward Euler Method')
plt.plot(x2,y2, label='f2 by Backward Euler Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

