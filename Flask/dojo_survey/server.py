from genericpath import exists
from flask import Flask, render_template, redirect, request, session
app= Flask(__name__)
app.secret_key = b'Ot[m\xc1l\xb8\x95\xa6"}\xce\xc2\x92A9'

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/results", methods=['POST','GET'])
def form_recieved():
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['currentStudent'] = 'currentStudent' in request.form
    return redirect("/display")


@app.route("/display")
def display():
    return render_template("form_success.html", name_on_template = session['name'], gender_on_template = session['gender'], location_on_template = session['location'], language_on_template = session['language'], current_student = session['currentStudent'], comments_on_template = session['comments'])

@app.route("/goback", methods=['POST'])
def go_back():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)