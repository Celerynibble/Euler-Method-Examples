import numpy as np
import matplotlib.pyplot as plt

#initial conditions
K = 2.3e2
q1 = 79
q2 = 2
m = 4 #units: amu
Q = q1*q2/m
t=20
dt = 10**(-5)
x = [-15]
y = [3] #impact parameter b
a = [[K*Q*x[0]/(x[0]**2+y[0]**2)**(3/2),K*Q*y[0]/(x[0]**2+y[0]**2)**(3/2)]]
v = [[50,0]]

#loop

for i in range(0,int(t/dt)):
    
    v_x = a[i][0]*dt + v[i][0]
    v_y = a[i][1]*dt + v[i][1]
    v.append([v_x,v_y])
    
    x.append(v[i][0]*dt+x[i])
    y.append(v[i][1]*dt+y[i])
    
    a_x = K*Q*x[i]/(x[i]**2+y[i]**2)**(3/2)
    a_y = K*Q*y[i]/(x[i]**2+y[i]**2)**(3/2)
    a.append([a_x,a_y])

#plot
X = np.array(x)
Y = np.array(y)

plt.figure(figsize=(7,7))
plt.title("initial velocity: {} fm/s".format(v[0]))
plt.plot(0,0,marker = 'o', ms = 10, mec= 'orange', mfc= "orange")
plt.plot(x,y, color="black")
plt.xlim(-20,20)
plt.ylim(-5,15)
plt.grid("true")
plt.legend(["nucleus","b={} fm".format(y[0])])

def ScatAngle(x,y,u='rad'):
    Ang = np.arctan((y[len(y)-1]-y[len(y)-2])/(x[len(x)-1]-x[len(x)-2]))
    if Ang>0:
        degAng = (180/np.pi)*Ang
    else:
        degAng = 180 + (180/np.pi)*Ang
        
    print("{} in radians. {} in degrees".format(Ang,degAng))
        
    if u == 'rad':
        return Ang
    if u == 'deg':
        return degAng
    else:
        ScatAngle(x, y)