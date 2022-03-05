import numpy as np
import matplotlib.axes 
import matplotlib.pyplot as plt


def Function(x, y):
    return (1/(np.sqrt( ((x-0.51)**2) + ((y-0.21)**2) ))) - (1/np.sqrt( ((x-0.51)**2) + ((y+0.21)**2) ))

def CentralDerivative_x(f,x,h, y): 
    d = 0.

    if h!=0:
        d = -(f(x+h, y)-f(x-h, y))/(2*h)
      
    return d

def CentralDerivative_y(f,y,h, x):
    d = 0.

    if h!=0:
        d = -(f(x, y+h)-f(x, y-h))/(2*h)
      
    return d


def CentralDerivative_x1(f,x,h, y): 
    d = 0.

    if h!=0:
        d = -(f(x+h, y)-f(x-h, y))/(2*h)
    
    return d

def CentralDerivative_y1(f,y,h, x):
    d = 0.

    if h!=0:
        d = -(f(x, y+h)-f(x, y-h))/(2*h)
      
    return d

xi, xf, h = 0., 1., 0.05
Npoints = int((xf-xi)/h+1)

x = np.linspace(xi,xf,Npoints)
y = np.linspace(xi,xf,Npoints)

matriz_ex = np.zeros((len(x), len(y)))
matriz_ey = np.zeros((len(x), len(y)))
for i in range(len(matriz_ex)): # y
    for j in range(len(matriz_ey[0])): # x
        ex = CentralDerivative_x(Function,x[j],h, y[i])
        ey = CentralDerivative_y(Function,y[i],h, x[j])
        magnitud = np.sqrt(ex**2 + ey**2)
        matriz_ex[i][j] = ex 
        matriz_ey[i][j] = ey

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel(r'$x[m]$',fontsize=10)
ax.set_ylabel(r'$y[m]$',fontsize=10)
ax.quiver(x, y, matriz_ex, matriz_ey, color="r")
ax.plot(x, np.zeros(len(x)), "--", color = "k", label="Conducting plane")
ax.plot(0.51, 0.21,'o', color='b', label="Electric Charge") 
ax.legend(loc='upper right')    
plt.show()