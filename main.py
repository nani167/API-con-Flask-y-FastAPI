from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
security = HTTPBasic()

USERS = {
    "nani": "Card-1616"
}

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    user_ok = credentials.username in USERS
    pass_ok = user_ok and USERS[credentials.username] == credentials.password
    if not (user_ok and pass_ok):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    return credentials.username

@app.get("/")
def home():
    return {"mensaje": "API FastAPI disponible."}

@app.get("/protegida")
def protegida(usuario: str = Depends(verify_credentials)):
    return {"mensaje": f"Acceso concedido a {usuario}!"}
