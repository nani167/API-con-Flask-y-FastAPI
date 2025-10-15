# API-con-Flask-y-FastAPI
Práctica de API segura con autenticación básica y documentación OpenAPI en Flask y FastAPI

Descripción
Este repositorio contiene dos ejemplos de aplicación de API REST seguras:

- Una realizada en Flask, con autenticación básica y documentación generada con Swagger UI (Flasgger).
- Una realizada en FastAPI, con autenticación básica y documentación automática en Swagger UI (OpenAPI).

Estructura
- app.py: Código fuente de la API en Flask.

- main.py: Código fuente de la API en FastAPI.

Instalación y ejecución:
Flask:

# (En la carpeta del proyecto Flask)
python3 -m venv venv
source venv/bin/activate
pip install flask flask_httpauth flasgger
python app.py
  - Accede a: http://localhost:5000/
  - Documentación Swagger UI: http://localhost:5000/apidocs


FastAPI:
# (En la carpeta del proyecto FastAPI)
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
  - Accede a: http://localhost:8000/
  - Documentación Swagger UI: http://localhost:8000/docs

Rutas y autenticación:
Método  |  Ruta        |  Autenticación  |  Descripción                              
--------+--------------+-----------------+-------------------------------------------
GET     |  /           |  No             |  Ruta pública, mensaje de disponibilidad  
GET     |  /protegida  |  Básica         |  Solo usuarios autenticados pueden acceder
      
      Usuario: nani
      Contraseña: Card-1616

Documentación:
- Flask: Swagger UI en /apidocs usando Flasgger.
- FastAPI: Documentación automática Swagger UI en /docs.

