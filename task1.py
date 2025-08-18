from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# E-commerce application
app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

#fake database
database = []

@app.post("/products")
def create_product(product: Product):
    database.append(product.dict())
    return{"message":"Product created successfully", "Product": product}

@app.get("/products")
def get_products():
    if not database:
        raise HTTPException(status_code=404, detail="No products found")
    return {"Products": database}

@app.get("/products/{product_id}")
def get_id_product(product_id: int):
    for product in database:
        if product["id"] == product_id:
            return {"Product": product}
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for i, existing_product in enumerate(database):
        if existing_product["id"] == product_id:
            database[i] = product.dict()
            return {"message":"Product updated successfully", "Product": product}
    raise HTTPException(status_code=404, detail="Product not found")

#project completed
