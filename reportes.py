import json
import csv
import os

def generateReports(json_filepath, csv_filepath):
    """ Genera un archivo CSV a partir de un archivo JSON que contiene una lista de diccionarios """
    try:
        # Verificar si el archivo JSON existe
        if not os.path.exists(json_filepath):
            print(f"Error: El archivo JSON no se encontró en '{json_filepath}'")
            return

        # Leer los datos del archivo JSON
        with open(json_filepath, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Asegurarse de que los datos son una lista de diccionarios
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            print(f"Error: El archivo JSON en '{json_filepath}' no contiene una lista de diccionarios válida.")
            return

        # Si la lista está vacía, no hay nada que escribir
        if not data:
            print("Advertencia: La lista de datos JSON está vacía. No se generará un archivo CSV.")
            return

        # Obtener todos los encabezados posibles de todos los diccionarios
        # Esto asegura que todas las columnas estén presentes en el CSV
        all_keys = set()
        for item in data:
            all_keys.update(item.keys())

        headers = list(all_keys)
        # Opcional: Ordenar los encabezados si se desea un orden específico
        # headers.sort()

        # Escribir los datos en el archivo CSV
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            # Escribir la fila de encabezados
            writer.writeheader()

            # Escribir cada fila de datos
            for row_data in data:
                # DictWriter automáticamente escribe los valores correspondientes a los fieldnames
                # y deja las celdas vacías si una clave no existe en row_data
                writer.writerow(row_data)

        print(f"Reporte CSV generado exitosamente en '{csv_filepath}'")

    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el archivo JSON en '{json_filepath}'. Asegúrate de que el formato sea correcto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

