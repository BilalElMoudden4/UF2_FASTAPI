from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., title="Name of the item", max_length=100)
    description: str = Field(None, title="Description of the item", max_length=300)
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    tax: float = Field(None, description="Tax applied to the item")

@app.post("/items/")
async def create_item(item: Item):
    return item
