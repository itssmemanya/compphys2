import numpy as np
import matplotlib.pyplot as plt
def f(t,x):
    g=10
    return [x[1],-g]
def sol(t):
    return -5 *(-10* t + t**2)
#For exact solution x'=50

a=0
b=10
n=100
h=(b-a)/n
t=np.linspace(a,b,n+1)
o=2  # order
alpha=0 # x(a)=alpha
beta=0  # x(b)=beta
    
def rk4(guess,f):
    i=1
    x=np.zeros((n+1,o))
    iv=[alpha,guess] # initial values for x and x'
    x[0,:]=iv
    while i<=n:
        k1=f(t[i-1],x[i-1,:])
        k1[:]=[t*h*0.5 for t in k1]
        k2=f(t[i-1]+h/2,x[i-1,:]+k1)
        k2[:]=[t*h*0.5 for t in k2]
        k3=f(t[i-1]+h/2,x[i-1,:]+k2)
        k3[:]=[t*h for t in k3]
        k4=f(t[i-1]+h/2,x[i-1,:]+k3)
        k1[:]=[t/3 for t in k1]
        k2[:]=[t*2/3 for t in k2]
        k3[:]=[t/3 for t in k3]
        k4[:]=[t*h/6 for t in k4]
        x[i,:]=x[i-1,:]+k1+k2+k3+k4
        i+=1
    return x

def rklast(guess):
    l=rk4(guess,f)
    return l[-1,0]

def bisection(guess1,guess2):
    if rklast(guess1)*rklast(guess2) >= 0:
        print("Bisection method failed.")
        return None
    a = guess1
    b = guess2
    tol=0.01
    it=0
    res=100
    temp = [(a + b)/2]
    ftemp = rklast(temp[-1])
    while res>tol and it<100:
        if rklast(a)*ftemp < 0:
            b = temp[-1]
        elif rklast(b)*ftemp < 0:
            a = temp[-1]
        elif ftemp == 0:
            print("Found exact solution.")
            return temp
        res=ftemp-beta
        it+=1
        temp.append((a + b)/2)
        ftemp = rklast(temp[-1])
    return temp;

xval=bisection(40,150)

xsol=sol(t)
x=[]
for i in range(len(xval)):
    x=rk4(xval[i],f)
    plt.plot(t,x[:,0], label='f by shooting Method for guess '+str(xval[i]))

plt.plot(t,xsol, label='Analytical solution',linestyle=':',linewidth=4)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()

  
