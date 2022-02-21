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
    
    ruta = r"C:\Users\Eduardo\Downloads\DatosExp111.csv"
    my_path = os.path.abspath(r"C:\Users\Eduardo\Downloads")
    
    i_rojo, v_rojo, i_verde, v_verde, i_amarillo, v_amarillo, i_azul, v_azul = np.loadtxt(ruta, unpack=True, delimiter=',', skiprows=1)

    i_rojo *= 1e-8
    i_amarillo *= 1e-8
    i_azul *= 1e-8
    i_verde *= 1e-8
    
    error_y = 0.001
    error_x = 0.25e-8
    

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Corriente\,[A]$',fontsize=10)
    ax.set_ylabel(r'$Voltaje\,[V]$',fontsize=10)

    ax.scatter(i_rojo, v_rojo, c='r',s=13,label='Datos LED rojo')
    plt.errorbar(i_rojo,v_rojo,yerr=error_y,xerr=error_x,fmt='r', ecolor='r')
    regr_rojo = stats.linregress(i_rojo,v_rojo)
    Y_rojo = i_rojo*regr_rojo.slope + regr_rojo.intercept
    plt.plot(i_rojo, Y_rojo, '--',color='darkred', label='Ajuste LED rojo')
    
    ax.scatter(i_amarillo, v_amarillo, c='yellow',s=13, label='Datos LED amarillo')
    plt.errorbar(i_amarillo,v_amarillo,yerr=error_y,xerr=error_x,fmt='yellow', ecolor='yellow')
    regr_amarillo = stats.linregress(i_amarillo,v_amarillo)
    Y_amarillo = i_amarillo*regr_amarillo.slope + regr_amarillo.intercept
    plt.plot(i_amarillo, Y_amarillo, '--',color='gold', label='Ajuste LED amarillo')
    
    plt.legend()
    plt.savefig('rojo-amarillo.png', dpi=300, bbox_inches='tight')
    #plt.show()
    
    
    
    
    
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.set_xlabel(r'$Corriente\,[A]$',fontsize=10)
    ax1.set_ylabel(r'$Voltaje\,[V]$',fontsize=10)

    ax1.scatter(i_azul, v_azul, c='dodgerblue',s=13,label='Datos LED azul')
    plt.errorbar(i_azul,v_azul,yerr=error_y,xerr=error_x,fmt='dodgerblue', ecolor='dodgerblue')
    regr_azul = stats.linregress(i_azul,v_azul)
    Y_azul = i_azul*regr_azul.slope + regr_azul.intercept
    plt.plot(i_azul, Y_azul, '--',color='blue', label='Ajuste LED azul')
    
    ax1.scatter(i_verde, v_verde, c='lime',s=13, label='Datos LED verde')
    plt.errorbar(i_verde,v_verde,yerr=error_y,xerr=error_x,fmt='lime', ecolor='lime')
    regr_verde = stats.linregress(i_verde,v_verde)
    Y_verde = i_verde*regr_verde.slope + regr_verde.intercept
    plt.plot(i_verde, Y_verde, '--',color='green', label='Ajuste LED verde')
    
    plt.legend()
    #plt.show()
    plt.savefig("azul-verde.png")
    

    print(f"rojo: {regr_rojo.slope} +- {regr_rojo.stderr}, {regr_rojo.intercept} +- {regr_rojo.intercept_stderr}.")
    print(f"amarillo: {regr_amarillo.slope} +- {regr_amarillo.stderr}, {regr_amarillo.intercept} +- {regr_amarillo.intercept_stderr}.")
    print(f"azul: {regr_azul.slope} +- {regr_azul.stderr}, {regr_azul.intercept} +- {regr_azul.intercept_stderr}.")
    print(f"verde: {regr_verde.slope} +- {regr_verde.stderr}, {regr_verde.intercept} +- {regr_verde.intercept_stderr}.")
    
    q = 1.602176634e-19
    
    valores_y = np.array([regr_azul.intercept*q,regr_verde.intercept*q,regr_amarillo.intercept*q,regr_rojo.intercept*q])
    
    long_azul = 469e-9 #nm
    long_verde = 567e-9
    long_amarillo = 590e-9
    long_rojo = 659e-9
    
    c_luz =  299792458 #m/s
    
    """
    Valores viejos
    freq_azul = 6.66e14
    freq_verde = 5.45e14
    freq_amarillo = 5.16e14
    freq_rojo = 4.62e14
    # http://academic.eb.com/levels/
    # https://www.britannica.com/science/color/The-visible-spectrum
    """
    freq_azul = c_luz/long_azul
    freq_verde= c_luz/long_verde
    freq_amarillo = c_luz/long_amarillo
    freq_rojo = c_luz/long_rojo
    
  
    
    valores_x = np.array([freq_azul, freq_verde, freq_amarillo, freq_rojo])
    print(valores_x)
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    ax2.set_ylabel(r'$ \mathrm{Energía\,cinética\,de\,los\,electrones}\, [J]$',fontsize=10)
    ax2.set_xlabel(r'$Frecuencia\,[Hz]$',fontsize=10)
    

    ax2.scatter(valores_x, valores_y, color = 'darkviolet')
    plt.errorbar(valores_x[0],valores_y[0],yerr=regr_azul.intercept_stderr*q,xerr=None,fmt='darkviolet', ecolor='darkviolet')
    plt.errorbar(valores_x[1],valores_y[1],yerr=regr_verde.intercept_stderr*q,xerr=None,fmt='darkviolet', ecolor='darkviolet')
    plt.errorbar(valores_x[2],valores_y[2],yerr=regr_amarillo.intercept_stderr*q,xerr=None,fmt='darkviolet', ecolor='darkviolet')
    plt.errorbar(valores_x[3],valores_y[3],yerr=regr_rojo.intercept_stderr*q,xerr=None,fmt='darkviolet', ecolor='darkviolet')
    regr_planck = stats.linregress(valores_x,valores_y)
    Y_planck = valores_x*regr_planck.slope + regr_planck.intercept
    plt.plot(valores_x, Y_planck, '--',color='purple', label='Ajuste')
    
    #plt.errorbar(valores_x[0],valores_y[0],yerr=regr_azul.intercept_stderr,xerr=None,fmt='lime', ecolor='lime')
    
    
    print(f"planck: {regr_planck.slope} +- {regr_planck.stderr}, {-regr_planck.intercept} +- {regr_planck.intercept_stderr}.")
    plt.savefig("planck.png")
    plt.show()

    

if __name__ == "__main__":
    main()