# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:44:02 2022

@author: SNB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#Actividad 2

#una rendija

plt.figure()
simple = pd.read_excel("doblerendija.xlsx")
micrometros = np.around(simple["micrometros1"].to_numpy(),5)[:39]
metros = micrometros/1000000
voltaje = np.around(simple["voltaje"].to_numpy(),5)[:39]

voltaje *= 0.3
metros*=2
def toAngle(metros, L):
    return np.arctan(metros/L)


#for l in np.linspace(0.28, 0.4, 3):
    #print(l)
    #angles = toAngle(metros, l)
    #print(angles)

plt.scatter(metros, voltaje, color="k")


#metros = toAngle(metros, 0.3)

print(metros)


angx = np.linspace(-0.008, 0.008, 100)

def f2 (theta, A, B):
    return A*(np.sin(B*np.sin(theta)))**2 / (B*np.sin(theta))**2

# B = pi*a/lambda
plt.plot(angx, f2(angx, 0.25, 390))

ajuste, cov = curve_fit(f2, metros, voltaje , p0=[0.25, 300])
print(ajuste) #A, B (importa B)
print("")
print(np.sqrt(np.diag(cov))) #Incertidumbres A y B


plt.plot(angx, f2(angx, ajuste[0], ajuste[1]))
plt.xlabel("Ángulo (rad)")
plt.ylabel("Voltaje (V)")

