import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def main():

    dataFile = pd.read_excel("doblerendija.xlsx")
    micrometros = dataFile["micrometros"].to_numpy()
    metros = micrometros/1000000
    voltajes = dataFile["voltajes"].to_numpy() 
    
    L = 0.5
    angulos = np.arctan(metros/L) 

    plt.figure()
    plt.scatter(angulos,voltajes) 
    
    x_values = np.linspace(-0.008,0.008,300)

    def f (theta,A,B,C):
        return A*(np.cos(B*np.sin(theta)))**2 * ((np.sin(C*np.sin(theta)))/(C*np.sin(theta)))**2

    popt,pcov = curve_fit(f, angulos, voltajes)
    y_values_fitted = f(x_values, popt[0], popt[1], popt[2])
    
    plt.plot(x_values,y_values_fitted)
    plt.xlabel("Ángulo (rad)")
    plt.ylabel("Voltaje (V)")
    plt.show()

if __name__ == "__main__":
    main()
    