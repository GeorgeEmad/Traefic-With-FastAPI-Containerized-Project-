from fastapi import FastAPI, Response

app = FastAPI()
products = [
    {"id":1, "name": "apple", "price": 1.0},
    {"id":2, "name": "banana", "price": 0.5},
    {"id":3, "name": "carrot", "price": 0.2},
]


@app.get("/")
def root():
    return "hi Fast Api "


@app.get("/products")
def get_products():
    return products


@app.get("/products/search")
def test(name:str, response: Response):
    filtered_products = [p for p in products if name.lower().strip() in p["name"].lower()]
    response.status_code = 200
    return filtered_products

@app.get("/products/search2")
def test2(name:str, response: Response):
    filtered_product = next((p for p in products if name.lower().strip() in p["name"].lower()), None)
    if(filtered_product == None):
        response.status_code = 404
        return {"message": "Product not found"}
    response.status_code = 200
    return filtered_product

@app.get("/products/{id}")
def get_product_by_id(id:int, response: Response):
    product = next((p for p in products if p["id"] == id), None)
    if(product == None):
        response.status_code = 404
        return {"message": "Product not found"}
    response.status_code = 200
    return product

@app.post("/products")
def create_prodcut(product: dict, response: Response):
    product["id"] = len(products) + 1
    products.append(product)
    response.status_code = 201
    return product
