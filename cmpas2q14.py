import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    #y''=2y'/t-2y/t^2+tlnt
    return [y[1],2*y[1]/t-2*y[0]/(t**2)+t*np.log(t)]

def sol(t):
    #y(t)=7t/4+)t^3/2)lnt-(3/4)t^3
    return 7*t/4+(t**3)*np.log(t)/2-3*(t**3)/4

a=1
b=2
h=0.001
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
iv=[1,0] # initial values for y and y'
o=2  # order

def euler(a,b,h,n,t,iv,o,f):
    i=1
    y=np.zeros((n+1,o))
    y[0,:]=iv
    while i<=n:
        s=f(t[i-1],y[i-1,:])
        for j in range(o):
            s[j]=h*s[j]
        temp=f(t[i-1],y[i-1,:])
        temp[:]=[t*h for t in temp]
        y[i,:]=y[i-1,:]+temp
        i+=1
    return y

y=euler(a,b,h,n,t,iv,o,f)
ysol=sol(t)
plt.plot(t,y[:,0], label='f by Euler Method')
plt.plot(t,ysol,label='Analytical Solution',linestyle=':',linewidth=4)
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
