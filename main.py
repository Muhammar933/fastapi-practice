from typing import Optional
from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def load_data():
    with open("books.json", "r") as file:
        return json.load(file)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/books")
def get_data():
    return {"books": load_data()}

# ✅ Search by name first so it doesn't conflict with book_id
@app.get("/books/search")
def get_books_by_name(name: Optional[str] = None):
    data = load_data()
    if not name:
        return {"error": "Please provide a name to search"}
    filtered_books = [
        book for book in data if name.lower() in book["title"].lower()
    ]
    if filtered_books:
        return {"books": filtered_books}
    raise HTTPException(status_code=404, detail="No books found with that name")

# ✅ Then book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    data = load_data()
    for book in data:
        if book["id"] == book_id:
            return {"book": book}
    raise HTTPException(status_code=404, detail="Book not found")
