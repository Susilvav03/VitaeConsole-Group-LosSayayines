from datetime import datetime
import json

GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

fileData = "data.json"

data = []

try:
    with open(fileData, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

def saveData():
    with open(fileData, 'w') as file:
        json.dump(data, file, indent=4)

def newCV():
    print("\n--- New CV ---")
    name = input("Complete name: ")
    document = input("ID Document number: ")
    bornDate = input("Born date (YYYY-MM-DD): ")
    email = input("Email address: ")
    phone = input("Phone number: ")
    address = input("Address: ")

    academicFormation = []
    while (input("Do you want to add an academic formation? (y/n): ").lower() == 'y'):
        formationInst = input("Formation institution: ")
        formationTitle = input("Formation Title: ")
        formationYear = input("Formation Years: ")
        academicFormation.append([formationInst, formationTitle, formationYear])

    professionalExpirience = []
    while (input("Do you want to add a professional experience? (y/n): ").lower() == 'y'):
        experienceCorporation = input("Company name: ")
        experienceCharge = input("Charge name: ")
        experiencePosition = input("Functions of the job: ")
        experienceDuration = input("Duration in the company: ")
        professionalExpirience.append([experienceCorporation, experienceCharge, experiencePosition, experienceDuration])
    
    references = []
    while (input("Do you want to add a reference? (y/n): ").lower() == 'y'):
        referencesName = input("Name of the reference contact: ")
        referencesRelation = input("Relation with the reference contact: ")
        referencesPhonenumber = input("Phone number of the reference contact: ")
        references.append([referencesName, referencesRelation, referencesPhonenumber])

    abilities = set()
    while (input("Do you want to add an ability or certification? (y/n): ").lower() == 'y'):
        abilities.add(input("Please enter the ability or certification: "))
    
    sheet = {
        "Name": name,
        "ID": (document, bornDate),
        "Contact": {
            "Phone_number": phone,
            "Email_Address": email,
            "Address": address
        },
        "Formation": academicFormation,
        "Experience": professionalExpirience,
        "References": references,
        "Abilities": list(abilities)
    }

    data.append(sheet)
    saveData()
    print(GREEN + f"✅ CV of '{name}' was registered correctly." + RESET)

def searchCV():
    print("\n--- Searching CV ---")
    for diccionario in data:
        for clave in diccionario:
            print(f"Clave: {clave}")

def updateCV():
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