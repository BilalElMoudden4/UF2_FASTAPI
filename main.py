from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola Mundo"}

@app.post("/")
def crear_Item(item: dict):
    return {"mensaje": "Item creado", "item": item}

