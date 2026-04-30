from number_generator import generate_password_number
from text_generator import generate_password_text
from utils import check_password_strength
from utils import check_password_strength, color_text

def main_menu():
    while True:
        print("\n=== PASSFORGE ===")
        print("1. Generar contraseña aleatoria (número)")
        print("2. Generar contraseña basada en texto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                length = int(input("Ingrese la longitud: "))

                if length < 6 or length > 26:
                    print("Error: la longitud debe estar entre 6 y 26")
                    continue
                #Estas dos son las funsiones creadas
                password = generate_password_number(length)
                strength = check_password_strength(password)

                print(f"\nContraseña generada: {password}")
                print(f"Nivel de seguridad: {color_text(strength, strength)}")

            except ValueError:
                print("Error: ingrese un número válido")

        elif opcion == "2":
            text = input("Ingrese el texto base: ").strip()

            if len(text) < 3 or len(text) > 20:
                print("Error: el texto debe tener entre 3 y 20 caracteres")
                continue

            password = generate_password_text(text)
            strength = check_password_strength(password)

            print(f"\nContraseña generada: {password}")
            print(f"Nivel de seguridad: {color_text(strength, strength)}")

        elif opcion == "3":
            print("Saliendo de PassForge...")
            break

        else:
            print("Opción inválida, intenta de nuevo")