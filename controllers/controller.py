from flask import render_template, request, redirect
from app import app
from models.library import library


@app.route("/")
def index():
    return redirect("/books")


@app.route("/books")
def books():
    book_list = library.book_list
    print(book_list)
    return render_template("books.html", title="Books", books=book_list)
