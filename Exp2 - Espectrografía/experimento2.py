import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from pylab import cm
import pandas as pd 
from scipy import stats
from sklearn.linear_model import LinearRegression
import os
    
def main():
    #plt.style.use('science')
    plt.style.use(['science','no-latex'])
    
    # violeta, azul, rojo
    pixels_list = np.array([1190,1337,1845]) # x
    pixels_list = np.array([0,1190,1337,1845]) # x
    pixels_list = np.array([0, 1/4 - 1/36,1/4 - 1/25,1/4 - 1/9])
    #lambdas_list = [0,410e-9,434e-9,656e-9] # y 
    #lambdas_list = [0,410,434,656] # y
    lambdas_list = [0,1/(410e-9),1/(434e-9),1/(656e-9)] # y
    #lambdas_list = [1/(410),1/(434),1/(656)] # y


    # 1. Calibración de líneas espectrales del hidrógeno
    
    pixels_list = np.array([0,1190,1337,1845]) # x
    lambdas_list = [0,410,434,656] # y
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Pixeles$',fontsize=10)
    ax.set_ylabel(r'$Longitud\,de\,onda\,[nm]$',fontsize=10)
    ax.set_title(r'Calibración de líneas espectrales de H',fontsize=10)

    ax.scatter(pixels_list, lambdas_list, c='k',s=10)
    #plt.errorbar(i_rojo,v_rojo,yerr=error_y,xerr=error_x,fmt='r', ecolor='r')
    regression = stats.linregress(pixels_list,lambdas_list)
    Y_regression = pixels_list*regression.slope + regression.intercept
    plt.plot(pixels_list, Y_regression, '--',color='darkred', label=r'$\lambda$ = 0.35 pixeles - 6.83')
    
    print(f'm = {regression.slope}, b = {regression.intercept}')
    
     
    plt.legend()
    plt.savefig('calibracion_hidrogeno.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Resultado: m = 0.35, b = -6.83
    
    func_conversion = lambda x: x*regression.slope + regression.intercept
    # recibe pixeles y devuelve la frecuencia equivalente en nm
    
    
    
    
    
    
    # 2. Hallar constante de Rydberg:
    
    xvalues_list = np.array([0,1/4 - 1/36,1/4 - 1/25,1/4 - 1/9])
    lambdas_list = 1/(func_conversion(np.array([1190,1337,1845]))*1e-9) # y
    lambdas_list = lambdas_list.tolist()
    lambdas_list.insert(0,0)

    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$\frac{1}{2^2} - \frac{1}{n^2}$',fontsize=10)
    ax.set_ylabel(r'$\frac{1}{\lambda}[m]$',fontsize=10)
    ax.set_title(r'Constante de Rydberg',fontsize=10)

    ax.scatter(xvalues_list, lambdas_list, c='k',s=10)
    #plt.errorbar(i_rojo,v_rojo,yerr=error_y,xerr=error_x,fmt='r', ecolor='r')
    regression = stats.linregress(xvalues_list,lambdas_list)
    Y_regression = xvalues_list*regression.slope + regression.intercept
    plt.plot(xvalues_list, Y_regression, '--',color='darkred', label=r'$m    = 10702743.36 m^-1$   ')
    
    print(f'm = {regression.slope}, b = {regression.intercept}')
    
     
    plt.legend()
    plt.savefig('rydberg.png', dpi=300, bbox_inches='tight')
    plt.show()
    
   
   
    # Línea amarilla doble del mercurio
    print(f'Las lineas dobles del mercurio son {func_conversion(382)}, {func_conversion(384)}')
    

if __name__ == "__main__":
    main()