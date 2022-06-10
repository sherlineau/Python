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

if __name__ == "__main__":
    app.run(debug = True)