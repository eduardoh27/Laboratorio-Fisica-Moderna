import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
from scipy.optimize import curve_fit

def main():
    
    
    #plt.style.use('science')
    plt.style.use(['science','no-latex'])
    
    print("Laboratorio FM: Exp8 - Carga masa nuevo")
    
    seguir = True
    while seguir == True:
        
        punto = input("\nIngrese el punto: ")
        
        if punto == '1':
            punto1()    
        elif punto == '2':
            punto2()
        elif punto == '3':
            punto3()    

       
        else:
            seguir = False
            """            
            print("Punto no encontrado")
            continuar = input("Desea continuar? (s/n): ")
            if continuar == 'n':
                seguir = False
            else:
                seguir = True
            """
            
    
    print("\nFin del programa")
        
def punto1():
    
    corriente = np.array([2, 2.5, 3, 4]) # x
    error_x = 0.001
    
    campo_magnetico = [0.12, 0.2, 0.28, 0.4] # y
    error_y = 0.01
    
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Corriente\,[A]$',fontsize=10)
    ax.set_ylabel(r'$Campo Magnético\,[mT]$',fontsize=10)
    ax.set_title('Campo magnético según corriente en el centro del arreglo', fontsize=10)
    
    ax.scatter(corriente, campo_magnetico, c='k',s=13, marker='o', label='Datos')
    regresion = stats.linregress(corriente,campo_magnetico)
    Y_campo = corriente*(regresion.slope) + regresion.intercept
    plt.plot(corriente, Y_campo, label='Ajuste lineal')
    
    for i in range(len(corriente)):
        plt.errorbar(corriente[i], campo_magnetico[i], yerr=error_y, xerr=error_x, fmt='r', ecolor='r')
    
    print(f"B = {round(regresion.slope,3)}*I + {round(regresion.intercept,3)}")
    print(f"incert. pendiete = {regresion.stderr},  incert. intercepto = {regresion.intercept_stderr}")
    #plt.legend()
    plt.savefig('carga_masa-punto1', dpi=300, bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    main()
    