from flask import Flask, render_template, request, redirect
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

# both routes will execute the home function to render index.html since they are on top of each other
@app.route ("/")
@app.route("/todos")
def get_all_todos():
    return render_template("index.html", first_name = "Sherline", list_todos = list_todos)

@app.route("/todo/new")
def display_create_todo():
    return render_template("todoForm.html")

#action routes
@app.route("/todo/new", methods = ['POST']) 
def create_todo():
    pass

if __name__ == "__main__":
    app.run(debug = True)
#this code is needed to run your environment and be in an active state when you run this file.

"""
urls can be reused as long as methods are different 
standards:
action routes -> recieve information but never render a template
takes us to another route that renders the template


GET - read and display
URL of route to display all: the name of list or dictionary we are about to display
Example: "/todos" 
Example: "/users"

Function: get_all_todos()

URL of route to display one: name of list in singular that we are about to display followed by the id
Example: "/todo/<int:id>"
Example: "/user/<int:id>"  (or string if user is a string)

Function: get_user_by_id( id )


POST - create
URL of route to create something new: name of list in singular that we are about to create followed by keyword /new
Example: "/todo/new"
Example: "/user/new"

Function:  create_todo()


PUT - update
URL of the route to update something already existing: name of the list in singular that we are about to update, followed by id, follwed by keyword /update or /edit
EXAMPLE: "/todo/<int:id>/update"
EXAMPLE: "/user/<int:id>/update"

Function: update_user_by_id( id )

DELETE - remove
URL of the route to delete something already existing:name of the list in singular that we are about to delete, followed by id, follwed by keyword /delete or /remove

Function: delete_todo_by_id( id )
"""