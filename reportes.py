from hojasDeVida import *
import csv



def generateReports():
    """
    Allows generating different reports based on CV data.
    """
    data = readData()
    print("\n--- Generate Reports ---")
    if not data:
        print("⚠️ No CVs registered.")
        return

    while True:
        option = input("\nReport Options:\n"
                       "1. List CVs with experience over N years\n"
                       "2. Candidates with specific certification or formation\n"
                       "3. Export CVs (complete or summarized - NOT IMPLEMENTED)\n"
                       "4. Back to main menu\n"
                       "Select an option: ")

        if option == '1':
            try:
                min_years = int(input("Enter the minimum years of experience: "))
                candidates = [cv for cv in data if
                              any(int(exp["duration"].split()[0]) > min_years and "year" in exp["duration"].lower()
                                  for exp in cv.get("professionalExperience", []))]
                if candidates:
                    print(f"\n--- Candidates with experience over {min_years} years ---")
                    for cv in candidates:
                        print(f"Name: {cv.get('name', 'N/A')}, Document: {cv.get('document', 'N/A')}")
                else:
                    print(f"❌ No candidates found with more than {min_years} years of experience.")
            except ValueError:
                print("❌ Please enter a valid number for years.")

        elif option == '2':
            term = input("Enter the specific certification or formation: ").lower()
            candidates = [cv for cv in data if
                          term in cv.get("abilities", "").lower() or
                          any(term in form["title"].lower() or term in form["institution"].lower()
                              for form in cv.get("academicFormation", []))]
            if candidates:
                print(f"\n--- Candidates with '{term}' in their formation or skills ---")
                for cv in candidates:
                    print(f"Name: {cv.get('name', 'N/A')}, Document: {cv.get('document', 'N/A')}")
            else:
                print(f"❌ No candidates found with '{term}'.")

        elif option == '3':
            print("⚠️ Exporting CVs is not implemented yet.")

        elif option == '4':
            break

        else:
            print("❌ Invalid option.")