import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def toAngle(metros, L=0.5):
        return np.arctan(metros/L)



#Actividad 2

#una rendija

def singleSlit():

    simple = pd.read_excel("doblerendija.xlsx")
    micrometros = np.around(simple["micrometros1"].to_numpy(),5)[:39]
    metros = micrometros/1000000
    voltaje = np.around(simple["voltaje"].to_numpy(),5)[:39]

    voltaje *= 0.3
    metros*=2
    


    #for l in np.linspace(0.28, 0.4, 3):
        #print(l)
        #angles = toAngle(metros, l)
        #print(angles)

    plt.figure()
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
    

def doubleSlit():

    dataFile = pd.read_excel(r"C:\Users\Eduardo\Downloads\Labs\LaboratorioDeFisicaModerna202220\ExpSofía - Doble rendija\doblerendija.xlsx")
    micrometros = dataFile["microsDobleCentered"].to_numpy()[:-3]
    metros = micrometros/1000000
    voltajes = dataFile["voltajeDoble"].to_numpy()[:-3]  
    #print(len(metros),"\n",len(voltajes))

    
    
    # MISSING ANGULOS (METROS->ANGULOS) 
    angulos = toAngle(metros) 
    #print(angulos)
    
    
    
    
    #solo se tienen en cuenta los valores entre -0.006 y 0.006  
    i = 0
    limites = []
    valor_limite = 0.008
    while i < len(angulos):
        if angulos[i] >= -valor_limite and len(limites) == 0:
            limites.append(i)
        
        elif angulos[i] >= valor_limite:
            limites.append(i)
            break
        i+=1
        
    #print(limites)
    #print(angulos[limites[0]:limites[1]])
    
    angulos = angulos[limites[0]:limites[1]]
    voltajes = voltajes[limites[0]:limites[1]]
    
    
    plt.figure()
    plt.scatter(angulos,voltajes, color='k') 
    # plt.errorbar(angulo, voltaje, xerr=0.00001, yerr = 0.005, fmt=" ")

    #thetax = np.linspace(-0.005,0.005,100)
    thetax = np.linspace(-valor_limite,valor_limite,300)

    def f1 (theta,A,B,C):
        return A*(np.cos(B*np.sin(theta)))**2 * ((np.sin(C*np.sin(theta)))/(C*np.sin(theta)))**2

    popt,pcov = curve_fit(f1,angulos, voltajes, p0=[2.6,2150,360])
    #bounds=([2.3,2000,500],[2.8,3000,600])
    yajuste = f1(thetax, popt[0], popt[1], popt[2])
    plt.plot(thetax,yajuste)
    plt.xlabel("Ángulo (rad)")
    plt.ylabel("Voltaje (V)")
    #print(popt) #A, B y C (importan B y C)
    #print(np.sqrt(np.diag(pcov))) #Incertidumbres A, B y C




def main():
    #singleSlit()
    doubleSlit()
    plt.show()

if __name__ == "__main__":
    main()