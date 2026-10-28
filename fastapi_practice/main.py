# from fastapi import FastAPI

# app = FastAPI()


# #Home Rout
# @app.get("/home")
# def home():
#     return {"Message":"Hello from FastAPI VENV"}


# #About Rout
# @app.get("/about")
# def about():
#     return {"Message":"This is About Page"}


# #USER Rout
# @app.get("/users")
# def users():
#     return {"users": ["Mohit", "Rohit", "Hamza"]}


from fastapi import FastAPI, status

app = FastAPI()

books = {1: {"title": "Dune"}}
books = {2: {"title": "HarryPorter"}}


@app.get("/books")
def list_books():
    return books

@app.post("/books")
def create_book():
    return {"message": "Book created"}

@app.put("/books/{book_id}")
def replace_book(book_id: int):
    return {"message": f"Book {book_id} replaced"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return {"message": f"Book {book_id} deleted"}


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book():
    return {"message": "Book created"}


from fastapi import HTTPException

@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = books.get(book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book