from hojasDeVida import registrar_hoja_de_vida, consultar_hojas_de_vida, actualizar_hoja_de_vida
from reportes import generar_reportes

def mostrar_menu():
    print("=== VitaeConsole ===")
    print("1. Registrar nueva hoja de vida")
    print("2. Consultar hojas de vida")
    print("3. Actualizar hoja de vida")
    print("4. Generar reportes")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_hoja_de_vida()
        elif opcion == "2":
            consultar_hojas_de_vida()
        elif opcion == "3":
            actualizar_hoja_de_vida()
        elif opcion == "4":
            generar_reportes()
        elif opcion == "5":
            print("Saliendo de VitaeConsole...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")

if __name__== "__main__":
    main()