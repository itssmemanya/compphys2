import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    #y'=(y^2+y)/t
    return (y**2+y)/t

def sol(t):
    #y(t)=-2t/(-1+2t)
    return -2*t/(-1+2*t)

a=1
b=3
n=100
h=(b-a)/n
t=np.linspace(a,b,n+1)
iv=-2 # initial value for y
o=1   # order

err=0.0001

def adapth(h,y1,y2):
    return h*((30*h*err)/(abs(y1-y2)))**0.25

def rk4(h,n,t,iv,f):
    i=1
    y=np.zeros((n+1,o))
    y[0]=iv
    while i<=n:
        y[i]=rk4it(t[i-1],y[i-1],h)
        i+=1
    return y

def rk4h(h,iv,f):
    i=1
    t=[a]
    y=[iv]
    while t[-1]<=b:
        y=np.append(y,rk4it(t[-1],y[-1],h))
        t=np.append(t,t[-1]+h)
        if i%2==0:
            y2=rk4it(t[i-2],y[i-2],2*h)
            h=adapth(h,y[-1],y2)
        i+=1
        if i>100:
            break
    return t,y

def rk4it(t,y,h):
     k1=h*f(t,y)
     k2=h*f(t+h/2,y+k1/2)
     k3=h*f(t+h/2,y+k2/2)
     k4=h*f(t+h/2,y+k3)
     return y+k1/6+k2/3+k3/3+k4/6    

y=rk4(h,n,t,iv,f)
t2=np.linspace(a,b,51)
t2,y2=rk4h(h,iv,f)
ysol=sol(t)
plt.plot(t,ysol, label='Analytical solution')
plt.scatter(t,y, label='f by RK4 Method with constant h',color='red')
plt.scatter(t2,y2, label='f by RK4 Method with adaptive h',color='yellow')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()

