import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit

def main():
    
    
    #plt.style.use('science')
    plt.style.use(['science','no-latex'])
    
    print("Laboratorio FM: Exp5 - Radioactividad")
    
    seguir = True
    while seguir == True:
        
        punto = input("\nIngrese el punto: ")
        
        if punto == '1':
            punto1()    
        elif punto == '21':
            punto21()
        elif punto == '22':
            punto22()
        elif punto == '3':
            punto3()    
        elif punto == '4':
            punto4()
       
        else:
            print("Punto no encontrado")
            continuar = input("Desea continuar? (s/n): ")
            if continuar == 'n':
                seguir = False
            else:
                seguir = True
    
    print("\nFin del programa")
        
def punto21():
    
    tiempo = [1]*3+[3]*3+[5]*3 # x
    error_x = 0.017
    
    conteo = [123,138,135,374,401,381,680,629,674] # y
    error_y = 1
    
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Tiempo\,[min]$',fontsize=10)
    ax.set_ylabel(r'$Conteo$',fontsize=10)
    #ax.set_title('Conteo según tiempo a una distancia de 5 cm',fontsize=10)
    
    ax.scatter(tiempo, conteo, c='b',s=13, marker='o', label='Datos')

    for i in range(len(tiempo)):
        plt.errorbar(tiempo[i], conteo[i], yerr=error_y, xerr=error_x, fmt='r', ecolor='r')
     
    plt.savefig('radioactividad-punto2', dpi=300, bbox_inches='tight')
    plt.show()


def punto22():
   
    tiempo = [1]*3+[3]*3+[5]*3 # x
    error_x = 0.017
    
    conteo = [0.817507418,0.795252226,0.799703264,0.445103858,
              0.40504451,0.434718101,0.038575668,0.066765579,0] # y
    error_y = 1
    
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Tiempo\,[min]$',fontsize=10)
    ax.set_ylabel(r'$1\,-\,conteo\,normalizado$',fontsize=10)
    #ax.set_title('Conteo según tiempo a una distancia de 5 cm',fontsize=10)
    
    ax.scatter(tiempo, conteo, c='b',s=13, marker='o', label='Datos')

    #for i in range(len(tiempo)):
    #    plt.errorbar(tiempo[i], conteo[i], yerr=error_y, xerr=error_x, fmt='r', ecolor='r')
     
    plt.savefig('radioactividad-poisson', dpi=300, bbox_inches='tight')
    plt.show()
    
   
   
   
   
def punto4():


    y = [370,357,345,335,128,127,123,135,84,79,82,96,
            66,62,52,57,51,38,49,50]
 
    x = [2]*4+[4]*4+[6]*4+[8]*4+[10]*4
    
    def func1(x, a, b):
        return a/np.polyval([1,0,0], x) +b #x**2
    
    def func2(x, a, b):
        return a/np.polyval([0,1,0], x) +b
    
    
    num = input('Ingrese el numero de funcion a utilizar: ')
    if num == '1':
        print("función cuadratica")
        func = func1
    else:
        print("función lineal")
        func = func2
        
    params, covs = curve_fit(func, x, y)

    perr = np.sqrt(np.diag(covs))
    print(f'perr = {perr}')
    
    y_fit = func(x, *params)
    
    # residual sum of squares
    ss_res = np.sum((y - y_fit) ** 2)

    # total sum of squares
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    # r-squared
    r2 = 1 - (ss_res / ss_tot)
        
    print(r2)
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Distancia\,[cm]$',fontsize=10)
    ax.set_ylabel(r'$Conteo$',fontsize=10)
    
    ax.scatter(x,y, label='Datos', c='b',s=13)
    ax.plot(np.linspace(2, 10, 1000), func(np.linspace(2, 10, 1000), *params), label='Ajuste', c='r')
    #plt.plot(np.linspace(2, 10, 1000), func(np.linspace(2, 10, 1000), params[0], params[1]))
    #plt.plot(np.linspace(2, 10, 1000), func(np.linspace(2, 10, 1000), params[0], params[1]))
    
    plt.legend()
    plt.savefig('radioactividad-distancia', dpi=300, bbox_inches='tight')
    plt.show()




if __name__ == "__main__":
    main()
