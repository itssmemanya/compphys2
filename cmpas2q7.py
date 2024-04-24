import numpy as np
import matplotlib.pyplot as plt

def sol(t):
    return -5 *(-10* t + t**2)
#For exact solution x'=50

a=0
b=10
n=100
h=(b-a)/n
g=10
t=np.linspace(a,b,n+1)
o=2  # order
alpha=0 # x(a)=alpha
beta=0  # x(b)=beta

y = np.zeros(n+1)
y[0]=alpha
y[-1]=beta
colors = ('purple', 'blue','green','yellow','orange')
j = 0
tol = 1e-5

for i in range(10**5):
    y_old = y.copy()
    y[1:-1] = (y[2:] + y[:-2] + g * h ** 2)/2
    if np.max(np.abs(y - y_old)) < tol:
        print(f" Converged after {i} iterations ")
        break

    # Plotting candidate solutions for iterations divisible by 2000
    if i % 2000 == 0 and i!=0 and j<=4:
        plt.plot(t, y, label=f'Candidate Solution {j + 1}', color=colors[j])
        j += 1

xsol=sol(t)

plt.plot(t,xsol, label='Analytical solution',linestyle=':',linewidth=4,color='black')
plt.plot(t, y, label='Numerical Solution',color='red')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()
