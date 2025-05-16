from tabulate import tabulate
import json
ARCHIVO_DATOS = "datos.json"

def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def registrar_hoja_de_vida():
    datos = cargar_datos()
    print("\n--- Registro de Hoja de Vida ---")
    nombre = input("Nombre completo: ")
    documento = input("Número de documento: ")
    correo = input("Correo electrónico: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    hoja = {
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "fecha_nacimiento": fecha_nacimiento,
        "telefono": telefono,
        "direccion": direccion,
        "formacion": [],
        "experiencia": [],
        "referencias": [],
        "habilidades": []
    }

    datos.append(hoja)
    guardar_datos(datos)
    print("✅ Hoja de vida registrada exitosamente.")

def consultar_hojas_de_vida():
    datos = cargar_datos()
    print("\n--- Consulta de Hojas de Vida ---")
    for idx, hoja in enumerate(datos, start=1):
        print(f"\n[{idx}] {hoja['nombre']} - {hoja['correo']}")

def actualizar_hoja_de_vida():
    datos = cargar_datos()
    print("\n--- Actualizar Hoja de Vida ---")
    documento = input("Ingrese el número de documento de la hoja a actualizar: ")
    for hoja in datos:
        if hoja["documento"] == documento:
            print(f"Editando hoja de vida de: {hoja['nombre']}")
            nuevo_telefono = input("Nuevo teléfono (dejar en blanco para no cambiar): ")
            if nuevo_telefono:
                hoja["telefono"] = nuevo_telefono
            guardar_datos(datos)
            print("✅ Datos actualizados.")
            return
    print("❌ No se encontró ninguna hoja con ese documento.")