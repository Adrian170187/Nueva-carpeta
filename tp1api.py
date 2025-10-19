from fastapi import FastAPI, HTTPException
app = FastAPI(title="TP1 API", version="1.0.0")
mensajes = []
contador=1

@app.get("/mensajes/")
def obtener_mensajes():
    return mensajes
