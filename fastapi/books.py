from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books") #decorator
async def read_all_books(category: str):
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        title = book.get("title")

        if not title:
            return

        if title.casefold() == book_title.casefold(): 
            return book

# Query params
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        cat = book.get("category")
        if not cat:
            return
        if cat.casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []

    for book in BOOKS:
        aut = book.get("author")
        cat = book.get("category")
        if not aut or not cat:
            return
        if aut.casefold() == book_author.casefold() and \
            cat.casefold() == category.casefold():
                books_to_return.append(book)

    return books_to_return

# Post
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

# Put
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold(): # type: ignore
            BOOKS[i] = updated_book

# Delete
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold(): # type: ignore
            BOOKS.pop(i)
            break

# Assignment => by author
@app.get("/books/author/{author_name}")
async def get_books_by_author(author_name: str):
    books_to_return = []
    for book in BOOKS:
        auth = book.get("author")
        if not auth:
            return
        if auth.casefold() == author_name.casefold():
            books_to_return.append(book)
    return books_to_return