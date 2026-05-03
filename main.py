from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "mensaje": "¡Despliegue automático verificado con éxito!",
        "estudiante": "Diego Jose Sierra Carcamo",
        "estado": "Finalizado y Verificado"
    }