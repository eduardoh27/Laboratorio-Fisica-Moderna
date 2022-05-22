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
        
        #print(f"len(corrientes), corrientes[0], corrientes[-1] = {len(corrientes), corrientes[0], corrientes[-1]}")
        #print(f"len(flujos), flujos[0], flujos[-1] = {len(flujos), flujos[0], flujos[-1]}")

        plt.figure()
        plt.plot(corrientes, flujos)
        plt.xlabel(xlabel="Corriente (A)")
        plt.ylabel(ylabel = "Flujo (Vs)")
        plt.title("Curva"+str(i))
        plt.savefig(git_route+"\Curva"+str(i)+".png")
                  
    print("OK")


if __name__ == "__main__":
    main()
    