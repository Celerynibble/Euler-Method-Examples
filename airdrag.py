import numpy as np
import matplotlib.pyplot as plt

#variables
dt=0.1
g=9.8
D=0.0245

#array initialization
t = np.arange(0,10,dt)
a = np.array([-g])
v = np.array([0])
y = np.array([2])

#computing values of array
for i in range(0,len(t)-1):
    a = np.append(a, [-g-D*v[i]*abs(v[i])])
    v = np.append(v, [a[i]*dt + v[i]])
    y = np.append(y, [v[i]*dt + y[i]])
    
plt.figure(3)

plt.subplot(1,3,1)
plt.plot(t,y)
plt.title("distance")
plt.xlabel("time")
plt.xticks([i for i in range(0,11,2)])
plt.ylabel("distance")

plt.subplot(1,3,2)
plt.plot(t,v)
plt.title("velocity")
plt.xlabel("time")
plt.xticks([i for i in range(0,11,2)])
plt.ylabel("velocity")

plt.subplot(1,3,3)
plt.plot(t,a)
plt.title("acceleration")
plt.xlabel("time")
plt.xticks([i for i in range(0,11,2)])
plt.ylabel("acceleration")

plt.tight_layout(pad=1.0)
