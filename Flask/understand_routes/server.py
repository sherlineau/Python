from ast import Num
from flask import Flask, render_template
app = Flask(__name__)

@app.route ("/")
def home():
    return "Hello World!"

@app.route ("/dojo")
def dojo():
    return "DOJO!"

@app.route ("/say/<str>")
def say( str ):
    str = str.capitalize()
    return f"Hi {str}!"

@app.route ("/repeat/<int:num>/<str>")
def repeat(num, str):
    return num * str

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug = True)