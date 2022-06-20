from flask import Flask, redirect, render_template, request
# import class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # call get all class method to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

# route for adding new friend to database
@app.route("/create_friend", methods=["POST"])
def create_friend():
    # make data dictionary from request form
    # keys will be variables in query string
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # pass data dictionary into save method from friend class
    Friend.save(data)
    # redirect
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)