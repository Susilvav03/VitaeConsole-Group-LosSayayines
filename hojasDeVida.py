import json
archiveData = "data.json"

def readData():
    try:
        with open(archiveData, 'r') as archive:
            return json.load(archive)
    except FileNotFoundError:
        return "No se encuentran Hojas de vida registradas"

def saveData(data):
    with open(archiveData, 'w') as archive:
        json.dump(data, archive, indent=4)

def newCV():
    data = readData()
    print("\n--- Registro de Hoja de Vida ---")
    name = input("name completo: ")
    document = input("Número de documento: ")
    email = input("Correo electrónico: ")
    bornDate = input("Fecha de nacimiento (YYYY-MM-DD): ")
    phone = input("Teléfono: ")
    address = input("Dirección: ")

    hoja = {
        "nombre": name,
        "documento": document,
        "correo": email,
        "fecha_nacimiento": bornDate,
        "telefono": phone,
        "direccion": address,
        "formacion": [],
        "experiencia": [],
        "referencias": [],
        "habilidades": []
    }

    data.append(hoja)
    saveData(data)
    print("✅ Hoja de vida registrada exitosamente.")

def changeCV():
    data = readData()
    print("\n--- Consulta de Hojas de Vida ---")
    for idx, hoja in enumerate(data, start=1):
        print(f"\n[{idx}] {hoja['name']} - {hoja['correo']}")

def updateCV():
    data = readData()
    print("\n--- Actualizar Hoja de Vida ---")
    document = input("Ingrese el número de documento de la hoja a actualizar: ")
    for hoja in data:
        if hoja["documento"] == document:
            print(f"Editando hoja de vida de: {hoja['name']}")
            newPhone = input("Nuevo teléfono (dejar en blanco para no cambiar): ")
            if newPhone:
                hoja["telefono"] = newPhone
            saveData(data)
            print("✅ data actualizados.")
            return
    print("❌ No se encontró ninguna hoja con ese documento.")