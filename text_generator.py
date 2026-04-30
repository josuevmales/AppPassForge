import random
import string

def generate_password_text(text: str) -> str:
    """
    Genera una contraseña segura basada en un texto del usuario.
    """

    # Validación
    if not isinstance(text, str) or not text:
        return ""
    
    # 2. Limpieza 
    text = text.strip()
    text = "".join(text.split())
    
    # 1. Normalizar y transformar
    text = text.lower()
    text = text.replace("a", "@") \
               .replace("e", "3") \
               .replace("i", "1") \
               .replace("o", "0") \
               .replace("s", "$")

    # 2. Mezclar mayúsculas y minúsculas
    nuevo_texto = ""
    for char in text:
        if random.choice([True, False]):
            nuevo_texto += char.upper()
        else:
            nuevo_texto += char.lower()

    # 3. Agregar refuerzo (números y símbolos)
    refuerzo = string.digits + string.punctuation
    for _ in range(3):  # agrega 3 caracteres extra
        nuevo_texto += random.choice(refuerzo)

    # 4. Mezclar todo (shuffle)
    lista = list(nuevo_texto)
    random.shuffle(lista)
    password = "".join(lista)

    return password