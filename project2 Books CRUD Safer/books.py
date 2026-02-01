from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException # to cancel the functionality of our method
from pydantic import BaseModel, Field
from starlette import status
app = FastAPI()
# uvicorn main:app --reload --host 127.0.0.1 --port 8080

class Book:
    def __init__(self, id: int, title: str, author: str, description: str, rating: float):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    title: str = Field(..., example="Brave New World", min_length=3, max_length=50)
    author: str = Field(..., example="Aldous Huxley", min_length=3, max_length=50)
    description: Optional[str] = Field(example="Science fiction novel", min_length=10, max_length=300)
    rating: float = Field(..., example=4.5, ge=0, le=6) 
    model_config = {"from_attributes" : True} # needs to be dict

    
BOOKS = [
    Book(1, "1984", "George Orwell", "Dystopian novel", 4.8),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "Classic novel", 4.7),
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Tragedy novel", 4.6),

]

@app.get("/books/", status_code=status.HTTP_200_OK)
def get_books():
    return BOOKS

@app.put("/books/", status_code=status.HTTP_201_CREATED)
def add_book(book: BookRequest):
    BOOKS.append(Book(id=new_id(), **book.model_dump()))
    return book
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int = Path(..., description="The ID of the book to retrieve", ge=1)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
@app.get("/books/search/", status_code=status.HTTP_200_OK)
def search_books(rating: Optional[str] = Query(gt=0,lt=6)):
    results = []
    for book in BOOKS:
        if rating and rating.casefold() in book.rating.casefold():
            results.append(book)
    raise HTTPException(status_code=404, detail="No books found with the given rating")


def new_id():
    if BOOKS:
        return BOOKS[-1].id + 1
    return 1
if __name__ == "__main__":
    import subprocess
    subprocess.run(["../../../fastapi_venv/Scripts/Activate"], shell=True)
    subprocess.run(["uvicorn", "books:app", "--reload", "--host", "127.0.0.1", "--port", "8080"])

