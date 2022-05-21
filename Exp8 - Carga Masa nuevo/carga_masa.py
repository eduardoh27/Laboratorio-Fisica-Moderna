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
    
    campo = [0.12, 0.2, 0.28, 0.4] # y
    error_y = 0.01
    
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Corriente\,[A]$',fontsize=10)
    ax.set_ylabel(r'$Campo\,Magnético\,[mT]$',fontsize=10)
    #ax.set_title('Campo magnético según corriente en el centro del arreglo', fontsize=10)
    
    ax.scatter(corriente, campo, c='k',s=13, marker='o', label='Datos')
    regresion = stats.linregress(corriente, campo)
    Y_campo = corriente*(regresion.slope) + regresion.intercept
    plt.plot(corriente, Y_campo, label='Ajuste lineal')
    
    for i in range(len(corriente)):
        plt.errorbar(corriente[i], campo[i], yerr=error_y, xerr=error_x, fmt='r', ecolor='r')
    
    print(f"B = {round(regresion.slope,4)}*I + {round(regresion.intercept,3)}")
    print(f"incert. pendiente = {round(regresion.stderr,4)},  incert. intercepto = {round(regresion.intercept_stderr,4)}")
    #plt.legend()
    plt.savefig('carga_masa-punto1', dpi=300, bbox_inches='tight')
    #plt.show()

    for i in range (1, 100):
        print(f'\ni= {i}')
        print(f"mag = {campo_magnetico(i)*1000}")
        print(f"exp = {campo_experimental(i)}")
    
def campo_experimental(I):
    return (0.1394 * I) - 0.151 # da en mT

def campo_magnetico(I):    
    miu_0 = 4*np.pi*(1e-7) 
    print(miu_0)
    N = 154
    R = 0.2
    resultado = miu_0*8*N/(np.sqrt(125)*R)
    print(resultado)
    print(resultado*1000) 
    return resultado * I # da en T
    
def campo_magnetico1(I,n,R,z,h):
    
    miu_0 = 4*np.pi*(1e-7)  # * 1000 #para que sean mT en vez de T
    n = 154
    R = 0.2
    
    return (miu_0*I*n*R*R / 2) * ( (1/((R*R+(z+h/2)**2)**(3/2))) + (1/((R*R+(z-h/2)**2)**(3/2))) )

def punto2():
    voltaje4 = np.array([100
    ,125
    ,150
    ,175
    ,200
    ,225
    ,250
    ,275])

    Bcuad4 = np.array([2.42736E-08,
    4.29443E-08,
    6.54746E-08,
    8.20593E-08,
    1.05872E-07,
    1.2278E-07,
    1.43035E-07,
    1.59241E-07
    ])
    
    voltaje6 = np.array([100,
    125,
    150,
    175,
    200,
    225,
    250,
    275,
    ])
    
    Bcuad6 = np.array([7.05398E-09,
    6.47194E-10,
    7.17172E-09,
    1.42889E-08,
    2.09173E-08,
    2.88049E-08,
    3.3731E-08,
    3.90458E-08,
    ])

    voltaje8 = np.array([150,
    175,
    200,
    225,
    250,
    275,
    ])
    
    Bcuad8 = np.array([4.22796E-10,
    2.34663E-09,
    4.43077E-09,
    6.93756E-09,
    9.72709E-09,
    1.33065E-08,
    ])

    voltaje10 = np.array([150,
    175,
    200,
    225,
    250,
    275,
    ])
    
    Bcuad10 = np.array([1.02131E-10,
    2.7332E-11,
    5.45222E-10,
    1.49645E-09,
    2.21351E-09,
    3.38724E-09,
    ])
    
    error_y = 1
    error_x = 0.01

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$B^2\,[T^2]$',fontsize=10)
    ax.set_ylabel(r'$Voltaje\,[V]$',fontsize=10)

    ax.scatter(Bcuad4, voltaje4, c='blue',s=13, marker='o')
    regresion4 = stats.linregress(Bcuad4, voltaje4)
    Y_4 = Bcuad4*(regresion4.slope) + regresion4.intercept
    plt.plot(Bcuad4, Y_4, label='Ajuste lineal', color='blue')
    
    ax.scatter(Bcuad6, voltaje6, c='pink',s=13, marker='o')
    regresion6 = stats.linregress(Bcuad6, voltaje6)
    Y_6 = Bcuad6*(regresion6.slope) + regresion6.intercept
    plt.plot(Bcuad6, Y_6, label='Ajuste lineal', color = 'pink')
    
    ax.scatter(Bcuad8, voltaje8, c='red',s=13, marker='o')
    regresion8 = stats.linregress(Bcuad8, voltaje8)
    Y_8 = Bcuad8*(regresion8.slope) + regresion8.intercept
    plt.plot(Bcuad8, Y_8, label='Ajuste lineal', color = 'red')
    
    ax.scatter(Bcuad10, voltaje10, c='green',s=13, marker='o')
    regresion10 = stats.linregress(Bcuad10, voltaje10)
    Y_10 = Bcuad10*(regresion10.slope) + regresion10.intercept
    plt.plot(Bcuad10, Y_10, label='Ajuste lineal', color = 'green')
    
    plt.savefig('carga_masa-punto2', dpi=300, bbox_inches='tight')

    plt.show()

if __name__ == "__main__":
    main()
    