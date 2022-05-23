import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

    
def main():
    plt.style.use(['science','no-latex'])

    git_route = r"C:\Users\Eduardo\Downloads\Labs\LaboratorioDeFisicaModerna202220\Exp11 - Histéresis Magnética"
    #excel_route = r"C:\Users\Eduardo\OneDrive - Universidad de los Andes\2022-1\Laboratorio de Física Moderna\Experimento11 - Histéresis Magnética\Datos Histéresis.Datos Histéresis.xlsx"
    #my_path = os.path.abspath(r"C:\Users\Eduardo\Downloads")
    
    df = pd.read_excel(git_route+"\Datos Histéresis.xlsx", sheet_name=None)
    #Curva5_GRIS = df["Curva5 GRIS"]
    
    for i in range(5, 13+1):

        
        print(f"\ni = {i}")
        
        sheet = df["Curva"+str(i)]
        corrientes = sheet["I_A1 / A"].dropna().to_numpy()
        flujos = sheet["&F / Vs"].dropna().to_numpy()
        
        saturacion = max(flujos)
        remanente = None
        coercitividad = None
        
        for tupla in zip(corrientes, flujos):
            corriente = tupla[0]
            flujo = tupla[1]
            if (corriente <= 0.02 and corriente > -0.01) :
                if flujo > 0 and flujo != 0:
                    remanente = flujo
            
            if (flujo <= 0.04 and flujo > -0.04) :
                if corriente > 0 and (corriente > 0.05 or corriente < -0.05):
                    coercitividad = corriente
            
        #print(f"len(corrientes), corrientes[0], corrientes[-1] = {len(corrientes), corrientes[0], corrientes[-1]}")
        #print(f"len(flujos), flujos[0], flujos[-1] = {len(flujos), flujos[0], flujos[-1]}")
        
        frecuencia = sheet["Frecuencia (Hz)"][0]
        voltaje = sheet["Voltaje (V)"][0]
        nucleo = sheet["Núcleo "][0]
        
        
        if nucleo == "Gris":
            nucleo = "Gris"    
            
            
        elif nucleo == "Negro":
            nucleo = "Negro"
            
            
        else:
            print("ERROR")
            
        #print(f"frecuencia, voltaje, nucleo = {frecuencia, voltaje, nucleo}")
        
        plt.figure()
        plt.plot(corrientes, flujos)
        plt.xlabel(xlabel="Corriente (A)")
        plt.ylabel(ylabel = "Flujo Magnético (V s)")
        plt.axvline(x=0, c="k")#, label="x=0")
        plt.axhline(y=0, c="k")#, label="y=0")
        
        plt.scatter(0, remanente, c="g", label = f"$m_r$ = {remanente} V s")
        plt.scatter(coercitividad, 0, c="r", label = f"coer. = {coercitividad} A")
        plt.axhline(y=saturacion, c="purple", label=f"sat. = {saturacion} V s")
        plt.legend()
        
        #plt.title(f"C{i}:  f = {frecuencia} Hz, V = {voltaje} V, núcleo = {nucleo}", size=10)
        plt.savefig(git_route+"\Curva"+str(i)+".png")
        
    print("\nOK\n")



def calculos():
    
    deltaL = 0.0005
    a = 0.04
    b = 0.15
    deltaV = np.sqrt((2*a*b*deltaL)**2 + (a*a*deltaL)**2)
    V = 0.04**2 * 0.15
    print(f"V = {V*1e6} +- {deltaV*1e6}")

    deltaM = 0.1/1000
    m = 1.5909
    print(f"m = {m} +- {deltaM}")
    
    
    deltaR = np.sqrt((deltaM/V)**2 + (-(m*deltaV)/(V**2))**2)
    rho = m/V
    print(f"rho = {rho} +- {deltaR}")



if __name__ == "__main__":
    
    main()
    None