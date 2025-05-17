import json

GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

fileData = "data.json"
reportData = "export.csv"
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

def saveData(data):
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
            if any(entry.get(["id"][0]) == document for entry in data):
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
    saveData(data)
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
            print(RED + "\n❌ Invalid option. Going back to Main menu." + RESET)

def searchCV():
    """ Search for a CV in the data """
    print("\n--- Searching CV ---")
    data = readData()
    key = input("Search by name, ID number or email: ")
    for resume in data:
        if key in resume["name"] or key in resume["id"][0] or key in resume["contact"]["email_Address"]:
            printCV(resume)
            
def filterCV():
    """ Filter CVs by abilities, formation or experience """
    data = readData()
    print("\n--- Filtering CVs ---")
    filterOption = input("Please enter the filter option (abilities, formation, experience): ").lower()
    
    if filterOption not in ["abilities", "formation", "experience"]:
        print(RED + "\n❌ Invalid filter option. Going back to Main menu" + RESET)
        return
    filterValue = input("Please enter the value to filter by: ")

    filteredCVs = []
    for sheet in data:
        if filterOption in sheet and filterValue in sheet[filterOption]:
            filteredCVs.append(sheet)

    if filteredCVs:
        print(GREEN + f"✅ Found {len(filteredCVs)} CV(s) matching the filter." + RESET)
        for cv in filteredCVs:
            printCV(cv)
    else:
        print(RED + "❌ No CVs found matching the filter. Going back to Main menu" + RESET)

def showAllCVs():
    """ Show all CVs in the data """
    data = readData()
    print("\n--- Showing All CVs ---")
    if not data:
        print(RED + "❌ No CVs found.  Going back to Main menu" + RESET)
        return
    for sheet in data:
        printCV(sheet)

def updateCV():
    """ Update an existing CV in the data based on the document part of the id """
    data = readData()
    print("\n--- Update CV ---")
    # Prompt for the document number to find the CV
    document_to_update = input("Enter the document number of the CV you want to update: ")
    found_index = -1

    # Search for the CV by the document number (first element of the 'id' tuple)
    for i, cv in enumerate(data):
        # Check if the 'id' key exists and is a tuple with at least one element
        if "id" in cv and isinstance(cv["id"], tuple) and len(cv["id"]) > 0 and cv["id"][0] == document_to_update:
            found_index = i
            break

    if found_index != -1:
        cv_update = data[found_index]
        # Access the name using the get method for safety
        print(f"\n--- Updating CV of: {cv_update.get('name', 'N/A')} ---")

        while True:
            # Display update options
            print("\nWhich section do you want to update?")
            print("1. Personal Data")
            print("2. Academic Formation")
            print("3. Professional Experience")
            print("4. References")
            print("5. Skills or Certifications")
            print("6. Back to main menu")

            option = input("\nEnter your choice: ")

            # Process user's choice
            if option == '1':
                updatePersonalData(cv_update)
            elif option == '2':
                updateAcademicFormation(cv_update)
            elif option == '3':
                updateProfessionalExperience(cv_update)
            elif option == '4':
                updateReferences(cv_update)
            elif option == '5':
                # Update abilities (assuming it's a list of strings)
                print("\n--- Update Skills or Certifications ---")
                # Ask for a comma-separated list and split into a list
                abilities_input = input("Enter the new skills or certifications (comma-separated): ")
                cv_update["abilities"] = [ability.strip() for ability in abilities_input.split(',') if ability.strip()]
            elif option == '6':
                # Exit the update loop
                break
            else:
                print("❌ Invalid option.")

        # Save the updated data
        saveData(data)
        print("✅ CV updated successfully.")
    else:
        print(f"❌ No CV found with the document number: {document_to_update}")


def updatePersonalData(cv):
    """Allows editing personal data within the new structure."""
    print("\n--- Edit Personal Data ---")
    # Access and update fields within the nested 'contact' dictionary and the top-level 'name'
    # Use .get() with a default empty dictionary for 'contact' for safety
    contact_info = cv.setdefault("contact", {})

    # Update name
    current_name = cv.get("name", "N/A")
    cv["name"] = input(f"Full Name ({current_name}): ") or current_name

    # Update contact details
    current_phone = contact_info.get("phone_number", "N/A")
    contact_info["phone_number"] = input(f"Contact Number ({current_phone}): ") or current_phone

    current_address = contact_info.get("address", "N/A")
    contact_info["address"] = input(f"Address ({current_address}): ") or current_address

    current_email = contact_info.get("email_Address", "N/A")
    contact_info["email_Address"] = input(f"Email Address ({current_email}): ") or current_email


def updateAcademicFormation(cv):
    """Allows adding new academic formation to the 'formation' list."""
    print("\n--- Add Academic Formation ---")
    # Ensure 'formation' key exists and is a list
    cv.setdefault("formation", [])

    while True:
        institution = input("Institution (leave blank to finish): ")
        if not institution:
            break
        title = input("Title Obtained: ")
        years = input("Years of Study: ")
        # Append new entry to the 'formation' list
        cv["formation"].append({"institution": institution, "title": title, "years": years})


def updateProfessionalExperience(cv):
    """Allows adding new professional experience to the 'experience' list."""
    print("\n--- Add Professional Experience ---")
    # Ensure 'experience' key exists and is a list
    cv.setdefault("experience", [])

    while True:
        company = input("Company Name (leave blank to finish): ")
        if not company:
            break
        charge = input("Position Held: ")
        functions = input("Job Functions: ")
        duration = input("Duration in the Company: ")
        # Append new entry to the 'experience' list
        cv["experience"].append({"company": company, "charge": charge, "functions": functions, "duration": duration})


def updateReferences(cv):
    """Allows adding new references to the 'references' list."""
    print("\n--- Add References ---")
    # Ensure 'references' key exists and is a list
    cv.setdefault("references", [])

    while True:
        name = input("Reference Name (leave blank to finish): ")
        if not name:
            break
        relation = input("Relation: ")
        phoneNumber = input("Phone Number: ")
        # Append new entry to the 'references' list
        cv["references"].append({"name": name, "relation": relation, "phoneNumber": phoneNumber})

def printCV(cv):
    """ Prints a CV dictionary in a readable and structured format """
    if not isinstance(cv, dict):
        print(RED + "Error: The provided data is not a valid CV dictionary." + RESET)
        return

    print("\n" + "="*40)
    print(f"{MAGENTA}--- Curriculum Vitae Information ---{RESET}")
    print("="*40)

    # --- Personal Data ---
    print(f"\n{YELLOW}--- Personal Data ---{RESET}")
    print(f"  {GREEN}Name:{RESET} {cv.get('name', 'N/A')}")

    # Handle the 'id' which is a tuple (document, bornDate)
    id_info = cv.get('id', ('N/A', 'N/A'))
    documento = id_info[0] if isinstance(id_info, tuple) and len(id_info) > 0 else 'N/A'
    fecha_nacimiento = id_info[1] if isinstance(id_info, tuple) and len(id_info) > 1 else 'N/A'
    print(f"  {GREEN}ID Document Number:{RESET} {documento}")
    print(f"  {GREEN}Date of Birth:{RESET} {fecha_nacimiento}")

    # --- Contact ---
    print(f"\n{YELLOW}--- Contact ---{RESET}")
    contact_info = cv.get('contact', {})
    print(f"  {GREEN}Phone Number:{RESET} {contact_info.get('phone_number', 'N/A')}")
    print(f"  {GREEN}Email Address:{RESET} {contact_info.get('email_Address', 'N/A')}")
    print(f"  {GREEN}Address:{RESET} {contact_info.get('address', 'N/A')}")

    # --- Academic Formation ---
    print(f"\n{YELLOW}--- Academic Formation ---{RESET}")
    formation_list = cv.get('formation', [])
    if formation_list:
        for i, formation in enumerate(formation_list):
            print(f"  {GREEN}Formation {i+1}:{RESET}")
            # Assuming each formation item is a list [institution, title, year]
            if isinstance(formation, list) and len(formation) >= 3:
                print(f"    Institution: {formation[0]}")
                print(f"    Title: {formation[1]}")
                print(f"    Year(s): {formation[2]}")
            # If formation is stored as a dictionary (as in the updateAcademicFormation function)
            elif isinstance(formation, dict):
                print(f"    Institution: {formation.get('institution', 'N/A')}")
                print(f"    Title: {formation.get('title', 'N/A')}")
                print(f"    Year(s): {formation.get('years', 'N/A')}")
            else:
                print(f"    Unknown formation format: {formation}")
    else:
        print("  No academic formation information.")

    # --- Professional Experience ---
    print(f"\n{YELLOW}--- Professional Experience ---{RESET}")
    experience_list = cv.get('experience', [])
    if experience_list:
        for i, experience in enumerate(experience_list):
            print(f"  {GREEN}Experience {i+1}:{RESET}")
            # Assuming each experience item is a list [company, charge, functions, duration]
            if isinstance(experience, list) and len(experience) >= 4:
                print(f"    Company: {experience[0]}")
                print(f"    Position: {experience[1]}")
                print(f"    Functions: {experience[2]}")
                print(f"    Duration: {experience[3]}")
            # If experience is stored as a dictionary (as in the updateProfessionalExperience function)
            elif isinstance(experience, dict):
                print(f"    Company: {experience.get('company', 'N/A')}")
                print(f"    Position: {experience.get('charge', 'N/A')}")
                print(f"    Functions: {experience.get('functions', 'N/A')}")
                print(f"    Duration: {experience.get('duration', 'N/A')}")
            else:
                print(f"    Unknown experience format: {experience}")
    else:
        print("  No professional experience information.")

    # --- References ---
    print(f"\n{YELLOW}--- References ---{RESET}")
    references_list = cv.get('references', [])
    if references_list:
        for i, reference in enumerate(references_list):
            print(f"  {GREEN}Reference {i+1}:{RESET}")
            # Assuming each reference item is a list [name, relation, phone]
            if isinstance(reference, list) and len(reference) >= 3:
                print(f"    Name: {reference[0]}")
                print(f"    Relation: {reference[1]}")
                print(f"    Phone Number: {reference[2]}")
            # If reference is stored as a dictionary (as in the updateReferences function)
            elif isinstance(reference, dict):
                print(f"    Name: {reference.get('name', 'N/A')}")
                print(f"    Relation: {reference.get('relation', 'N/A')}")
                print(f"    Phone Number: {reference.get('phoneNumber', 'N/A')}")
            else:
                print(f"    Unknown reference format: {reference}")
    else:
        print("  No reference information.")

    # --- Skills and Certifications ---
    print(f"\n{YELLOW}--- Skills and Certifications ---{RESET}")
    abilities_list = cv.get('abilities', [])
    if abilities_list:
        # Assuming abilities are a list of strings
        print("  " + ", ".join(abilities_list))
    else:
        print("  No skills or certifications listed.")

    print("\n" + "="*40)




 
	



	
