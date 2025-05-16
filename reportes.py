import json
import csv

archiveData = "data.json"

def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def generateReports():
    datos = cargar_datos()
    print("\n--- Generador de Reportes ---")
    opcion = input("¿Desea exportar todos los datos en CSV? (s/n): ").lower()
    if opcion == "s":
        with open("exportado.csv", "w", newline='') as archivo_csv:
            campos = ["nombre", "documento", "correo", "telefono"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
            escritor.writeheader()
            for hoja in datos:
                escritor.writerow({k: hoja[k] for k in campos})
        print("✅ Reporte exportado como exportado.csv")