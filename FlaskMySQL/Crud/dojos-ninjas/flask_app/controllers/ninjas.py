from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app
from flask import render_template, request, redirect

@app.route('/ninjas/new')
def new():
    return render_template("create_ninja.html",dojos = Dojo.get_all())

@app.route('/ninjas/create', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        id = request.form['dojo_id']
        Ninja.save(request.form)
        return redirect(f"/dojos/{id}")