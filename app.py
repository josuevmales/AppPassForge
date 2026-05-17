from flask import Flask, render_template, request
from number_generator import generate_password_number
from text_generator import generate_password_text
from utils import check_password_strength

app = Flask(__name__)

# 🔹 INTERFAZ 1 (HOME)
@app.route("/")
def index():
    return render_template("index.html")


# 🔹 INTERFAZ 2 (NÚMERO)
@app.route("/number", methods=["GET", "POST"])
def number():
    password = None
    strength = None
    error = None

    if request.method == "POST":

        length_input = request.form.get("length")

        # 1. Validar vacío
        if not length_input:
            error = "Ingrese un número"

        # 2. Validar que sea número
        elif not length_input.isdigit():
            error = "Solo se permiten números"

        else:
            length = int(length_input)

            # 3. Validar rango
            if length < 8 or length > 14:
                error = "La longitud debe estar entre 8 y 14"

            # 4. Crea contraseña
            else:
                password = generate_password_number(length) 
                strength = check_password_strength(password)

    return render_template(
        "number.html",
        password=password,
        strength=strength,
        error=error
    )

#------------------------------------------------------------------------------------------
# 🔹 INTERFAZ 3 (TEXTO)



# 🔻 SIEMPRE AL FINAL
if __name__ == "__main__":
    app.run(debug=True)