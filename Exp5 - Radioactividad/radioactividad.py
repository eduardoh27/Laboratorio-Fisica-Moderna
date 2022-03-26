import matplotlib.pyplot as plt
import numpy as np
import math 

def main():
    
    #plt.style.use('science')
    plt.style.use(['science','no-latex'])
    
    
    tiempo = [1]*3+[3]*3+[5]*3 # x
    error_x = 0.017
    
    conteo = [123,138,135,374,401,381,680,629,674] # y
    error_y = 1
    
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Tiempo [min]$',fontsize=10)
    ax.set_ylabel(r'$Conteo$',fontsize=10)
    ax.set_title('Conteo según tiempo a una distancia fija de 5 cm',fontsize=13)
    
    ax.scatter(tiempo, conteo, c='b',s=13, marker='o', label='Datos')

    for i in range(len(tiempo)):
        plt.errorbar(tiempo[i], conteo[i], yerr=error_y, xerr=error_x, fmt='r', ecolor='r')
     
    plt.savefig('Exp5 - Radioactividad - Punto 2', dpi=300, bbox_inches='tight')
    plt.show()
    

if __name__ == "__main__":
    main()
