from fastapi import FastAPI, HTTPException
app = FastAPI(title="TP1 API", version="1.0.0")
mensajes = []
contador=1

@app.get("/mensajes/")
def obtener_mensajes():
    return mensajes

@app.get("/mensajes/{mensajes_id}")
def obtener_mensaje(mensajes_id: int):
    for mensaje in mensajes:
        if mensaje["id"] == mensajes_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

@app.post("/mensajes/")
def crear_mensaje(mensaje: str):
    global contador
    nuevo_mensaje = {"id": contador, "mensaje": mensaje}
    mensajes.append(nuevo_mensaje)
    contador += 1
    return nuevo_mensaje
@app.put("/mensajes/{mensajes_id}")
def actualizar_mensaje(mensajes_id: int, mensaje: str):
    for msg in mensajes:
        if msg["id"] == mensajes_id:
            msg["mensaje"] = mensaje
            return msg
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
@app.delete("/mensajes/{mensajes_id}")
def eliminar_mensaje(mensajes_id: int):
    for i, msg in enumerate(mensajes):
        if msg["id"] == mensajes_id:
            del mensajes[i]
            return {"detail": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")