from flask import render_template, request, redirect
from app import app
from models.library import library


@app.route("/")
def index():
    return redirect("/books")


@app.route("/books")
def books():
    book_list = library.book_list
    return render_template("books.html", title="Books", books=book_list)


@app.route("/books", methods=["POST"])
def add_book():
    form = request.form
    library.add_book(form["title"], form["author"], form["genre"])
    return redirect("/books")


@app.route("/books/delete/<index>", methods=["POST"])
def remove_book(index):
    library.remove_book_by_index(int(index))
    return redirect("/books")


@app.route("/books/<index>")
def book(index):
    book = library.book_list[int(index)]
    return render_template("book-page.html", title="Books", book=book)
