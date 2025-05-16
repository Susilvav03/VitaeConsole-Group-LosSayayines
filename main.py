from hojasDeVida import newCV, searchCV, updateCV
from reportes import generateReports

GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def show_menu():
    """ Mostrar el menú """
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

def main():
    while True:
        show_menu()
        option = input("Please select an option(1-5): ")

        match option:
            case "1":
                newCV()
            case "2":
                searchCV()
            case "3":
                updateCV()
            case "4":
                generateReports()
            case "5":
                print("Thanks for using VitaeConsole...")
                break
            case _:
                    print("Invalid option. Try again.")

main()