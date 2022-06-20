from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

from flask_app import app

@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def dojos():
    return render_template("home.html", dojos = Dojo.get_all())

@app.route('/dojos/new', methods=['POST'])
def createDojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def showDojo(id):
    data = {
        "id":id
    }
    current_dojo = Dojo.get_one_with_ninjas(data)
    return render_template("dojo.html", current_dojo = current_dojo )
