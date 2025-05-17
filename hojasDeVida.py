import json

GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

fileData = "data.json"
flag = True

def readData():
    """
    Reads data from the JSON file.
    Returns an empty list if the file does not exist, is empty, or invalid.
    Handles errors using try-except without using os.
    """
    try:
        with open(fileData, 'r') as archive:
            # Try to load data. If the file is empty or not valid JSON,
            # json.load() will raise json.JSONDecodeError.
            data = json.load(archive)
            return data
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list.
        print(f" ⚠️ File '{fileData}' not found. A new one will be created upon saving.")
        return []
    except json.JSONDecodeError:
        # If the file is empty or contains invalid JSON, return an empty list.
        print(f"⚠️ The file '{fileData}' is empty or corrupt. Starting with empty data.")
        return []
    except Exception as e:
        # Catch any other unexpected errors.
        print(f" ⚠️ An unexpected error occurred while reading '{fileData}': {e}")
        return []

def saveData():
    """ Save the data to a JSON file """
    with open(fileData, 'w') as file:
        json.dump(data, file, indent=4)

def newCV():
    sheet = []
    """ Add a new CV to the data """
    data = readData()
    print("\n--- Adding New CV ---")
    name = input("Complete name: ")
    while flag:
        document = input("ID Document number: ")
        if document.isdigit():
        # Check if document number already exists
            if any(entry.get("Document") == document for entry in data):
                print(f"⚠️ A CV with document number {document} already exists.")
            else:
                break
        else:
            print("❌ Document number must contain only digits.")
    while True:
        bornDate = input("Born date (YYYY-MM-DD): ")
        # Simple date format validation
        if len(bornDate) == 10 and bornDate[4] == '-' and bornDate[7] == '-':
            break
        else:
            print("❌ Incorrect date format. Please use YYYY-MM-DD.")
    while flag:
        email = input("Email address: ")
        if "@" not in email or "." not in email:
            print("⚠️ Invalid email address format.")
        else:
            break
    while flag:
        phone = input("Phone number: ")
        if phone.isdigit():
            break
        else: 
            print("❌ Phone number must contain only digits.")
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
    
    # Create a dictionary for the CV
    sheet = {
        "name": name,
        "id": (document, bornDate),
        "contact": {
            "phone_number": phone,
            "email_Address": email,
            "address": address
        },
        "formation": academicFormation,
        "experience": professionalExpirience,
        "references": references,
        "abilities": list(abilities)
    }

    data.append(sheet)
    saveData()
    print(GREEN + f"✅ CV of '{name}' was registered correctly." + RESET)

def consultCV():
    """ Consult an existing CV in the data """
    print("\n--- Consulting CV ---")
    print("1. Search by document number, name or email")
    print("2. Filter by abilities, formation or experience")
    print("3. Show all CVs")

    option = input("Please select an option(1-3): ")
    match option:
        case "1":
            searchCV()
        case "2":
            filterCV()
        case "3":
            showAllCVs()
        case _:
            print(RED + "\nInvalid option. Going back to Main menu." + RESET)

def searchCV():
    """ Search for a CV in the data """
    print("\n--- Searching CV ---")
    data = readData()
    key = input("Search by name, ID number or email: ")
    for resume in data:
        if key in resume["name"] or key in resume["id"][0] or key in resume["contact"]["email_Address"]:
            print(data(resume, indent=4))
def filterCV():
    """ Filter CVs by abilities, formation or experience """
    data = readData()
    print("\n--- Filtering CVs ---")
    filterOption = input("Please enter the filter option (abilities, formation, experience): ").lower()
    
    if filterOption not in ["abilities", "formation", "experience"]:
        print(RED + "❌ Invalid filter option. Going back to Main menu" + RESET)
        return
    filterValue = input("Please enter the value to filter by: ")

    filteredCVs = []
    for sheet in data:
        if filterOption in sheet and filterValue in sheet[filterOption]:
            filteredCVs.append(sheet)

    if filteredCVs:
        print(GREEN + f"✅ Found {len(filteredCVs)} CV(s) matching the filter." + RESET)
        for cv in filteredCVs:
            print(cv)
    else:
        print(RED + "❌ No CVs found matching the filter. Going back to Main menu" + RESET)

def showAllCVs():
    """ Show all CVs in the data """
    print("\n--- Showing All CVs ---")
    if not data:
        print(RED + "❌ No CVs found.  Going back to Main menu" + RESET)
        return
    for sheet in data:
        print(sheet)

def updateCV():
    """ Update an existing CV in the data """
    print("\n--- Updating CV ---")
    document = input("Please enter the document number that you would like to update: ")
    for sheet in data:
        if sheet["Document"] == document:
            print(f"Changing CV of: {sheet['name']}")
            newPhone = input("New phone number (Please leave this space in blank if you don´t want to update): ")
            if newPhone:
                sheet["Phone_number"] = newPhone
            saveData(data)
            print(GREEN + f"✅ Data updated for '{"name"}'")
            return
    print(RED + "❌ No CV found with this document number. Going back to Main menu" + RESET)