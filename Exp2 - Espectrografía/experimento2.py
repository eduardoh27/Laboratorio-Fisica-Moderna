import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from pylab import cm
from scipy import stats
    
def main():
    
    #plt.style.use('science')
    plt.style.use(['science','no-latex'])
    
    
    """
    #pixels_list = np.array([1190,1337,1845]) # x
    #pixels_list = np.array([0,1190,1337,1845]) # x
    #pixels_list = np.array([0, 1/4 - 1/36,1/4 - 1/25,1/4 - 1/9])
    #lambdas_list = [0,410e-9,434e-9,656e-9] # y 
    #lambdas_list = [0,410,434,656] # y
    #lambdas_list = [0,1/(410e-9),1/(434e-9),1/(656e-9)] # y
    #lambdas_list = [1/(410),1/(434),1/(656)] # y
    """

    # 1. Calibración de líneas espectrales del hidrógeno
    
    pixels_list = np.array([0,254,285,393]) # x
    error_x = 1
    
    # violeta, azul, rojo
    lambdas_list = [0,410.17056,434.0471,656.2854] # y
    error_y = [0,0.0001,0.0003,0.0003]
    
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$Pixeles$',fontsize=10)
    ax.set_ylabel(r'$Longitud\,de\,onda\,[nm]$',fontsize=10)
    ax.set_title(r'Calibración de líneas espectrales de H',fontsize=10)

    ax.scatter(pixels_list, lambdas_list, c='k',s=10)
    #plt.errorbar(i_rojo,v_rojo,yerr=error_y,xerr=error_x,fmt='r', ecolor='r')
    regressionCalibracion = stats.linregress(pixels_list,lambdas_list)
    Y_regressionCalibracion = pixels_list*regressionCalibracion.slope + regressionCalibracion.intercept
    plt.plot(pixels_list, Y_regressionCalibracion, '--',color='darkred', label=r'$\lambda$ = 0.35 pixeles - 6.83')
    
    plt.errorbar(pixels_list[1],lambdas_list[1],yerr=error_y[1],xerr=error_x,fmt='r', ecolor='r')
    plt.errorbar(pixels_list[2],lambdas_list[2],yerr=error_y[2],xerr=error_x,fmt='r', ecolor='r')
    plt.errorbar(pixels_list[3],lambdas_list[2],yerr=error_y[3],xerr=error_x,fmt='r', ecolor='r')
    
    print(f'm = {regressionCalibracion.slope} +- {regressionCalibracion.stderr}, b = {regressionCalibracion.intercept} +- {regressionCalibracion.intercept_stderr}')
    
     
    plt.legend()
    plt.savefig('Exp2 - Espectrografía/calibracion_hidrogeno.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Resultado: m = 0.35, b = -6.83
    
    func_conversion = lambda x: x*regressionCalibracion.slope + regressionCalibracion.intercept
    # recibe pixeles y devuelve la frecuencia equivalente en nm
    
    
    
    
    
    
    # 2. Hallar constante de Rydberg:
    
    xvalues_list = np.array([0,1/4 - 1/36,1/4 - 1/25,1/4 - 1/9])
    lambdas_list = 1/(func_conversion(pixels_list[1:])*1e-9) # y
    lambdas_list = lambdas_list.tolist()
    lambdas_list.insert(0,0)

    y_error = lambda x: regressionCalibracion.slope / (regressionCalibracion.slope*x + regressionCalibracion.intercept)**2
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$\frac{1}{2^2} - \frac{1}{n^2}$',fontsize=10)
    #ax.set_ylabel(r'$\frac{1}{\lambda}[m]$',fontsize=10)
    ax.set_ylabel(r'$Longitud\,de\,onda^{-1}\,[m^{-1}]$',fontsize=10)
    ax.set_title(r'Constante de Rydberg',fontsize=10)

    ax.scatter(xvalues_list, lambdas_list, c='k',s=10)
    #plt.errorbar(i_rojo,v_rojo,yerr=error_y,xerr=error_x,fmt='r', ecolor='r')
    regressionRydberg = stats.linregress(xvalues_list,lambdas_list)
    Y_regressionRydberg = xvalues_list*regressionRydberg.slope + regressionRydberg.intercept
    plt.plot(xvalues_list, Y_regressionRydberg, '--',color='darkred', label=r'$m    = 10702743.36 m^-1$   ')
    
    plt.errorbar(xvalues_list[0],lambdas_list[0],yerr=y_error(pixels_list[1]),fmt='r', ecolor='r')
    plt.errorbar(xvalues_list[1],lambdas_list[1],yerr=y_error(pixels_list[2]),fmt='r', ecolor='r')
    plt.errorbar(xvalues_list[2],lambdas_list[2],yerr=y_error(pixels_list[3]),fmt='r', ecolor='r')

    
    print(f'\nRydberg:\nm = {regressionRydberg.slope} +- {regressionRydberg.stderr}, b = {regressionRydberg.intercept} +- {regressionRydberg.intercept_stderr}')
    
    
     
    plt.legend()
    plt.savefig('Exp2 - Espectrografía/rydberg.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    
   
    # 3. Línea amarilla doble del mercurio
    print(f'\nLas lineas dobles del mercurio son {func_conversion(360)}, {func_conversion(362)}')
    print(f'\nLas lineas dobles del mercurio son {1.6*382-7}, {3}')
    

if __name__ == "__main__":
    main()