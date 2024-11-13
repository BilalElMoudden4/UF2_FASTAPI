from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

# Definim el model de dades amb BaseModel
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    tax: Optional[float] = None  # Camp opcional
    category: str

# Diccionari per emmagatzemar els ítems
items: Dict[int, Item] = {}

# Endpoint GET per obtenir un ítem per ID
@app.get("/items/{item_id}")
def leer_item(item_id: int):
    if item_id in items:
        return items[item_id]
    else:
        # Retorna un error 404 si l'ítem no es troba
        raise HTTPException(status_code=404, detail="Item no encontrado")

# Endpoint POST per crear un ítem nou
@app.post("/items/")
def crear_Item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Ya existe un item con este ID")
    items[item.id] = item
    return item
