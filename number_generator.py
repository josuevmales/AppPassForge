import random
import string

def generate_password_number(length: int) -> str:
    """
    Genera una contraseña aleatoria basada en una longitud dada.
    Incluye letras, números y símbolos.
    """

    # Validación básica
    if not isinstance(length, int) or length <= 0:
        return ""

    caracteres = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(caracteres) for _ in range(length))

    return password