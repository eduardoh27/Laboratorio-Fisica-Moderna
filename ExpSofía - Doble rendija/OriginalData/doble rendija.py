#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:19:34 2022

@author: camilo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Actividad 1

xval1 = np.array([0,1,2])
yval1 = np.array([0.01, 1.24, 2.06])
ylin1 = (yval1)

linea = np.polyfit(xval1, ylin1,1)
grado2 = np.polyfit(xval1, ylin1, 2)

x = np.linspace(0,2.5,100)
plt.scatter(xval1, ylin1, color="k")
plt.plot(x, linea[0]*x+linea[1])
plt.plot(x, grado2[0]*x**2 + grado2[1]*x + grado2[2])
plt.errorbar(xval1, ylin1, yerr = 0.005, fmt=" ")

plt.xlabel("Número de rendijas")
plt.xticks([0,1,2])
plt.ylabel("Voltaje (V)")

#actividad 2
#doble rendija

doble = pd.read_csv("doble rendija.csv")
angulo = np.around(doble["theta (rad)"].to_numpy(), 5)
voltaje = doble["Voltaje (V)"].to_numpy()
plt.figure()
plt.scatter(angulo,voltaje, color='k') 
plt.errorbar(angulo, voltaje, xerr=0.00001, yerr = 0.005, fmt=" ")

thetax = np.linspace(-0.005,0.005,100)

def f1 (theta,A,B,C):
    return A*(np.cos(B*np.sin(theta)))**2 * ((np.sin(C*np.sin(theta)))/(C*np.sin(theta)))**2

popt,pcov = curve_fit(f1,angulo, voltaje, p0=[2.5,2300,500])
bounds=([1,2000,500],[3,3000,600])
yajuste = f1(thetax, popt[0], popt[1], popt[2])
plt.plot(thetax,yajuste)
plt.xlabel("Ángulo (rad)")
plt.ylabel("Voltaje (V)")
print(popt) #A, B y C (importan B y C)
print("")
print(np.sqrt(np.diag(pcov))) #Incertidumbres A, B y C
print("")
print("")

#una rendija

plt.figure()
simple = pd.read_csv("datos una rendija.csv")
ang = np.around(simple["theta"].to_numpy(),5)
volt = simple["voltaje"].to_numpy()
plt.scatter(ang, volt, color="k")

angx = np.linspace(-0.008, 0.008, 100)
 
def f2 (theta, A, B):
    return A*(np.sin(B*np.sin(theta)))**2 / (B*np.sin(theta))**2

ajuste, cov = curve_fit(f2, ang, volt, p0=[0.25, 300])
print(ajuste) #A, B (importa B)
print("")
print(np.sqrt(np.diag(cov))) #Incertidumbres A y B

plt.plot(angx, f2(angx, ajuste[0], ajuste[1]))
plt.xlabel("Ángulo (rad)")
plt.ylabel("Voltaje (V)")



