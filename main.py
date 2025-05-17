from hojasDeVida import *
from reportes import *

def show_menu():
    """ Display the main menu of the VitaeConsole application """
    print(MAGENTA + "\n _________________________________________________" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "|              Welcome to VitaeConsole            |" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "|---------------------- Menu ---------------------|" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)
    print(MAGENTA + "|                                                 |" + RESET)
    print(MAGENTA + "| 1. Add new CV                                   |" + RESET)
    print(MAGENTA + "| 2. Consult CV                                   |" + RESET)
    print(MAGENTA + "| 3. Update CV                                    |" + RESET)
    print(MAGENTA + "| 4. Generate reports                             |" + RESET)
    print(MAGENTA + "| 5. Exit                                         |" + RESET)
    print(MAGENTA + "|_________________________________________________|" + RESET)

# Main program loop
while flag:
    show_menu()
    option = input("\nPlease select an option(1-5): ")

    match option:
        case "1":
            newCV()
        case "2":
            consultCV()
        case "3":
            updateCV()
        case "4":
            generateReports(fileData,reportData)
        case "5":
            print("\nThanks for using VitaeConsole...")
            break
        case _:
            print(RED + "\nInvalid option. Try again." + RESET)
