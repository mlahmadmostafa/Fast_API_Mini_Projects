from fastapi import FastAPI, Body

app = FastAPI()
# uvicorn books:app --reload
# fastapi run books.py
# fastapi dev books.py
# http://127.0.0.1:8000/docs for docs, called swagger ui
BOOKS = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]
@app.get("/books") # decorative
def read_all_books():
    return BOOKS

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict = Body()):
    for i, book in enumerate(BOOKS):
        if book['id'] == book_id:
            BOOKS[i] = updated_book
            return updated_book
    return {"error": "Book not found"}
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(BOOKS):
        if book['id'] == book_id:
            deleted_book = BOOKS.pop(i)
            return deleted_book
    return {"error": "Book not found"}
@app.post("/books/add")
def add_book(book: dict = Body()):
    BOOKS.append(book)
    return book


# We put the static path before the dynamic path to avoid conflicts
@app.get("/books/latest") # static param
def read_latest_book():
    return BOOKS[-1]

@app.get("/books/{book_id}") # dynamic param
def read_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}
# it auto aligns the query param with second function argument
# example: /books/F%20Scott%20Fitzgerald/?title=The%20Great%20Gatsby
@app.get("/books/{author}/") # query param
def read_book_with_query(author: str, title: str = None):
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            if book.get("title").casefold() == title.casefold():
                return book
            return None
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload = True)