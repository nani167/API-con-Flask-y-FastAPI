from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)  # Inicializa Swagger para documentar la API
auth = HTTPBasicAuth()

# Datos de usuario para autenticación básica
USERS = {
    "nani": "Card-1616"
}

@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None

@app.route('/')
def home():
    """
    Ruta pública que muestra el estado de la API
    ---
    responses:
      200:
        description: API disponible
        examples:
          text: API Flask disponible.
    """
    return 'API Flask disponible.'

@app.route('/protegida')
@auth.login_required
def protegida():
    """
    Ruta protegida con autenticación básica
    ---
    security:
      - BasicAuth: []
    responses:
      200:
        description: Acceso autorizado
        examples:
          json:
            mensaje: Acceso concedido a nani!
      401:
        description: Error de autenticación
    """
    return jsonify({"mensaje": f"Acceso concedido a {auth.current_user()}!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)





