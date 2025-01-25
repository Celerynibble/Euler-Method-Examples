import numpy as np
import matplotlib.pyplot as plt

#initial conditions
G = 3
M = 3
dt = 10**(-5)
r = 1
x = [r]
y = [0]
v = [[1,1]] #initial velocity
a = [[-G*M/r**2,0]] #initial acceleration

#loops
for i in range(0,10**6):
    p = a[i][0]*dt + v[i][0]
    q = a[i][1]*dt + v[i][1]
    v.append([p,q])
    
    x.append(v[i][0]*dt + x[i])
    y.append(v[i][1]*dt + y[i])
    
    k = -G*M*x[i]/(x[i]**2 + y[i]**2)**(3/2)
    l = -G*M*y[i]/(x[i]**2+y[i]**2)**(3/2)
    a.append([k,l])
    
#plot

X = np.array(x)
Y = np.array(y)

plt.figure(figsize=(7,7))
plt.title("initial position: [{},{}] initial velocity: {}".format(x[0],y[0],v[0]))
plt.plot(0,0, marker = 'o', ms= 10, mec= "orange", mfc= "orange")
plt.plot(X,Y, color="black")
plt.xlim(min(X)-0.5, max(X)+0.5)
plt.ylim(min(Y)-0.5, max(Y)+0.5)
plt.grid("true")
plt.legend(["sun","trajectory"])