import json
archiveData = "data.json"

def readData():
    try:
        with open(archiveData, 'r') as archive:
            return json.load(archive)
    except FileNotFoundError:
        return []

def saveData(data):
    with open(archiveData, 'w') as archive:
        json.dump(data, archive, indent=4)

def newCV():
    data = readData()
    print("\n--- CV registered ---")
    name = input("Complete name: ")
    document = input("Document number: ")
    email = input("Email address: ")
    bornDate = input("Born date (YYYY-MM-DD): ")
    phone = input("Phone number: ")
    address = input("Address: ")
    formationInst = input("Formation institution: ")
    formationTitle = input("Formation Title: ")
    formationYear = input("Formation Years: ")
    experienceCorporation = input("Company name: ")
    experienceCharge = input("Charge name: ")
    experiencePosition = input("Functions of the job: ")
    experienceDuration = input("Duration in the company: ")
    referencesName = input("Name of the reference contact: ")
    referencesRelation = input("Relation with the reference contact: ")
    referencesPhonenumber = input("Phone number of the reference contact: ")
    abilities = input("Please enter the abilities or certifications: ")
    
    sheet = {
        "Name": name,
        "Document": document,
        "Email Address": email,
        "Born_date": bornDate,
        "Phone_number": phone,
        "Address": address,
        "Formation": [formationInst,formationTitle,formationYear],
        "Experience": [experienceCorporation,experienceCharge,experiencePosition,experienceDuration],
        "References": [referencesName,referencesRelation,referencesPhonenumber],
        "Abilities": abilities
    }

    data.append(sheet)
    saveData(data)
    print("✅ CV registered correctly.")

def searchCV():
    data = readData()
    print("\n--- Searching CV ---")
    for diccionario in data:
        for clave in diccionario:
            print(f"Clave: {clave}")

def updateCV():
    data = readData()
    print("\n--- Updating CV ---")
    document = input("Please enter the document number that you would like to update: ")
    for sheet in data:
        if sheet["Document"] == document:
            print(f"Changing CV of: {sheet['name']}")
            newPhone = input("New phone number (Please leave this space in blank if you don´t want to update): ")
            if newPhone:
                sheet["Phone_number"] = newPhone
            saveData(data)
            print("✅ data updated.")
            return
    print("❌ No CV found with this document number.")