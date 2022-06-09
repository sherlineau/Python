from flask import Flask 
#importing Flask, Flask is now a class.

app = Flask(__name__)

@app.route ("/hello/class")
def hello_from_flask():
    return "Hello! this is from flask"

@app.route ("/number/<int:num>")
def print_number( num ):
    print ("number sent from URL", num)
    return ( f"your number is {num}")


if __name__ == "__main__":
    app.run(debug = True)
#this code is needed to run your environment and be in an active state when you run this file.

