import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f1(t,y):
    #y'=t*e^(3t)-2y
    return t*np.exp(3*t)-2*y

def f2(t,y):
    #y'=1-(t-y)^2
    return 1-(t-y)**2

def f3(t,y):
    #y'=1+y/t
    return 1+y/t

def f4(t,y):
    #y'=cos 2t+sin 3t
    return np.cos(2*t)+np.sin(3*t)

def f1sol(t):
    #y(t)=(1/25)*(e^-2t)*(1+(e^(5t))*(5t-1))
    return (1/25)*(np.exp(-2*t))*(1+np.exp(5*t)*(5*t-1))

def f2sol(t):
    #y(t)=(1-3t+t^2)/(-3+t)
    return (1-3*t+t**2)/(-3+t)

def f3sol(t):
    #y(t)=2t+t*ln t
    return 2*t+t*np.log(t)

def f4sol(t):
    #y(t)=1/6(8-2cos(3t)+3sin(2t))
    return (1/6)*(8-2*np.cos(3*t)+3*np.sin(2*t))

y1=solve_ivp(f1,[0,1],[0])
t=np.linspace(0,1,100)
y1s=f1sol(t)
fig, ax = plt.subplots(2, 2)
plt.subplot(2,2,1)
plt.plot(y1.t,y1.y[0], label='f1 by solve_ivp')
plt.plot(t,y1s, label='f1 Analytical solution')
plt.title('$y′=t*e^{3t}-2y,y(0)=0$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

y2=solve_ivp(f2,[2,2.99],[1])#y is inf at 3
t=np.linspace(2,2.99,100)
y2s=f2sol(t)
plt.subplot(2,2,2)
plt.plot(y2.t,y2.y[0], label='f2 by solve_ivp')
plt.plot(t,y2s, label='f2 Analytical solution')
plt.title('$y′=1-{(t-y)}^2,y(2)=1$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

y3=solve_ivp(f3,[1,2],[2])
t=np.linspace(1,2,100)
y3s=f3sol(t)
plt.subplot(2,2,3)
plt.plot(y3.t,y3.y[0], label='f3 by solve_ivp')
plt.plot(t,y3s, label='f3 Analytical solution')
plt.title('$y′=1+y/t,y(1)=2$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

y4=solve_ivp(f4,[0,1],[1])
t=np.linspace(0,1,100)
y4s=f4sol(t)
plt.subplot(2,2,4)
plt.plot(y4.t,y4.y[0], label='f4 by solve_ivp')
plt.plot(t,y4s, label='f4 Analytical solution')
plt.title('$y′=cos 2t+sin 3t,y(0)=1$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
fig.tight_layout()
plt.show()
