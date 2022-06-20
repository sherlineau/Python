from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

# display all users
@app.route('/users')
def users():
    return render_template("index.html", users = User.get_all())

# create new users -> renders form for new users
@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods = ['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

# show one user
@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("show_user.html" , user = User.get_one(data))

# edit users
@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html" , user = User.get_one(data))
    
# update user
@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

# delete user
@app.route('/user/destroy/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/users')
