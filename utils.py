#futuras funciones útiles

import string

def check_password_strength(password: str) -> str:
    """
    Evalúa la fortaleza de una contraseña.
    Retorna: 'Débil', 'Media' o 'Fuerte'
    """

    if not password:
        return "Débil"
    #Mide que tan larga es la contraseña
    length = len(password)

    # Verificaciones
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    # Clasificación
    if length < 6:
        return "Débil"

    if length >= 10 and has_lower and has_upper and has_digit and has_symbol:
        return "Fuerte"

    return "Media"


#ANSI
def color_text(text, level):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    if level == "Débil":
        return f"{RED}{text}{RESET}"
    elif level == "Media":
        return f"{YELLOW}{text}{RESET}"
    elif level == "Fuerte":
        return f"{GREEN}{text}{RESET}"
    else:
        return text