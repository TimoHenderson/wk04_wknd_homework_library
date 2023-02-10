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
    return render_template("book-page.html", title="Books", book=book, index=index)


@app.route("/books/<index>", methods=["POST"])
def check_book_in_or_out(index):
    check_out = request.form["check_out"]
    request_origin = request.form["request_origin"]
    library.check_book_in_or_out(int(index), int(check_out))
    return redirect(request_origin)


@app.route("/books/update/<index>", methods=["POST"])
def update_book(index):
    form = request.form
    request_origin = request.form["request_origin"]
    library.update_book(int(index), form["title"], form["author"], form["genre"])
    return redirect(request_origin)
