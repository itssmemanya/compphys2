import numpy as np
import matplotlib.pyplot as plt
# Let dy/dt=y/t-(y/t)^2   (same as Q2)
def f(t,y):
    return y/t-(y/t)**2

def sol(t):
    return t/(1+np.log(t))
a=1
b=2
n=10
h=(b-a)/n
t=np.linspace(a,b,n+1)
iv=[1] # initial values 
o=1  

def rk6(t,f):
    i=1
    y=np.zeros((n+1,o))
    y[0,:]=iv
    s=np.sqrt(21)
    while i<=n:
        k1=h*f(t[i-1],y[i-1,:])
        k2=h*f(t[i-1]+h,y[i-1,:]+k1)
        k3=h*f(t[i-1]+h/2,y[i-1,:]+(3*k1+k2)/8)
        k4=h*f(t[i-1]+2*h/3,y[i-1,:]+(8*k1+2*k2+8*k3)/27)
        k5=h*f(t[i-1]+(7-s)*h/14,y[i-1]+
               (3*(3*s-7)*k1-8*(7-s)*k2+48*(7-s)*k3-3*(21-s)*k4)/392)
        k6=h*f(t[i-1]+(7+s)*h/14,y[i-1]+
               (-5*(51*s+231)*k1-40*(7+s)*k2-320*s*k3+3*(21+121*s)*k4+
                392*(6+s)*k5)/1960)
        k7=h*f(t[i-1]+h,y[i-1]+(15*(7*s+22)*k1+120*k2+40*(7*s-5)*k3-
                63*(3*s-1)*k4-14*(49+9*s)*k5+70*(7-s)*k6)/180)
        y[i,:]=y[i-1,:]+(9*k1+64*k3+49*k5+49*k6+9*k7)/180
        i+=1
    return y

y=rk6(t,f)
ysol=sol(t)
plt.plot(t,y[:,0], label='y(t) by RK6 method')
plt.plot(t,ysol, label='Analytical solution',linestyle=':',linewidth=4)
plt.title('For RK6 method calculates f 7 times in each step. \n I did 10 iterations,\
 thus a total of 70 evaluations.')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()
