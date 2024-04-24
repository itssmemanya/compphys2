import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def f1(x,y):
    #y''=-e^(-2y)
    return np.vstack((y[1],-np.exp(-2*y[0])))
def bc1(a,b):
    return np.array([a[0]-0,b[0]-np.log(2)])

def f2(x,y):
    #y''=y'cos x − y ln y
    return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))
def bc2(a,b):
    return np.array([a[0]-1,b[0]-np.exp(1)])

def f3(x,y):
    #y''=-(2(y')^3+(y^2)y')sec x
    return np.vstack((y[1],-(2*y[1]**3 + (y[0]**2)*y[1])/np.cos(x)))
def bc3(a,b):
    return np.array([a[0]-(2)**(-0.25),b[0]-(12**0.25)/2])

def f4(x,y):
    #y''=1/2 -(y')^2/2-y sin x /2
    return np.vstack((y[1],0.5-0.5*y[1]**2-y[0]*np.sin(x)/2))
def bc4(a,b):
    return np.array([a[0]-2,b[0]-2])

x1 = np.linspace(1, 2, 100)
x2 = np.linspace(0, np.pi/2, 100)
x3 = np.linspace(np.pi/4, np.pi/3, 100)
x4 = np.linspace(0, np.pi, 100)

y1 = np.zeros((2, x1.size))
y2 = np.ones((2, x2.size))
y3 = np.zeros((2, x3.size))
y4 = np.zeros((2, x4.size))

sol1 = solve_bvp(f1, bc1, x1, y1)
sol2 = solve_bvp(f2, bc2, x2, y2)
sol3 = solve_bvp(f3, bc3, x3, y4)
sol4 = solve_bvp(f4, bc4, x4, y4)

fig, ax = plt.subplots(2, 2)
plt.subplot(2,2,1)
plt.plot(sol1.x,sol1.y[0], label='f1 by solve_bvp')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('$y′′=−e^{−2y},y(1)=0,y(2)=ln 2$')
plt.legend()

plt.subplot(2,2,2)
plt.plot(sol2.x,sol2.y[0], label='f2 by solve_ivp')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('$y′′=y′cos x−yln y,y(0)=1,y(\pi/2)=e$')
plt.legend()

plt.subplot(2,2,3)
plt.plot(sol3.x,sol3.y[0], label='f3 by solve_bvp')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title(' $y′′=−(2(y′)^{3}+y^{2}y′)sec x,y( \pi /4)=2^{-1/4},\
y( \pi /3) =12^{1/4}/2$')
plt.legend()

plt.subplot(2,2,4)
plt.plot(sol4.x,sol4.y[0], label='f4 by solve_bvp')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('$y′′=1/2-(y′)^2/2-y sin x/2,y(0)=2,y(\pi)=2$')
plt.legend() 
fig.tight_layout()
plt.show()
