from flask import Flask, render_template
app = Flask(__name__)

list_todos = [
    {
    "todo" : "Learn templates in flask",
    "status" : "In Progress"
    } ,
    {
    "todo" : "Learn Object Oriented Programming",
    "status" : "Complete"
    } ,
    {
    "todo" : "Learn development",
    "status" : "Cancel"
    }
]

@app.route ("/hello/class")
def hello_from_flask():
    return "Hello! this is from flask"

@app.route ("/number/<int:num>")
def print_number( num ):
    print ("number sent from URL", num)
    return ( f"your number is {num}")

# both routes will execute the home function to render index.html since they are on top of each other
@app.route ("/")
@app.route("/home")
def home():
    return render_template("index.html", first_name = "Sherline", list_todos = list_todos)


if __name__ == "__main__":
    app.run(debug = True)
#this code is needed to run your environment and be in an active state when you run this file.

