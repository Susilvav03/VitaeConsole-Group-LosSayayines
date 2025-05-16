from hojasDeVida import *
import csv



def generateReports():
    """ Generate reports from the CV data """
    print("\n--- Generador de Reportes ---")
    opcion = input("¿Desea exportar todos los datos en CSV? (s/n): ").lower()
    if opcion == "s":
        with open("exportado.csv", "w", newline='') as archivo_csv:
            campos = ["nombre", "documento", "correo", "telefono"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            for hoja in data:
                escritor.writerow({k: hoja[k] for k in campos})
        print("✅ Reporte exportado como exportado.csv")