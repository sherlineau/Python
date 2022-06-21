from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models import book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def display_authors():
    return render_template("authors.html", authors = Author.get_all_users())

@app.route('/authors/new', methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        'id':id
    }
    current_author = Author.get_one_with_books(data)
    return render_template("author_info.html", current_author = current_author ,books = book.Book.get_all_books())

@app.route('/authors/newfavorite', methods=['POST','GET'])
def new_fav():
    if request.method == 'POST':
        id = request.form['user_id']
        Author.save_fav(request.form)
        return redirect(f'/authors/{id}')

