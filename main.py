from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensaje": "Bienvenida a mi aplicación web en Azure",
        "estudiante": "Katherine Monterroso",
        "estado": "Despliegue Inicial"
    }