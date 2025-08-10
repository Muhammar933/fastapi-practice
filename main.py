from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def load_data():
    with open("books.json","r") as file:
        data = json.load(file)
        return data

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/books")
def get_data():
    data = load_data()
    return {"books": data}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    data = load_data()
    for book in data:
        if book["id"] == book_id:
            return {"book": book}
    raise HTTPException(status_code=404, detail="Book not found")