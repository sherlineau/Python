from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.book import Book
from flask_app.models import author

@app.route('/books')
def display_books():
    return render_template("books.html", books = Book.get_all_books())

@app.route('/books/new', methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data = {
        'id':id
    }
    current_book = Book.get_book_with_users(data)
    return render_template("book_info.html", current_book = current_book, authors = author.Author.get_all_users())

@app.route('/books/newfavorite', methods=['POST','GET'])
def author_fav():
    if request.method == 'POST':
        id = request.form['book_id']
        Book.save_fav(request.form)
        return redirect(f'/books/{id}')
