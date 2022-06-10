from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
        return redirect("/play")
@app.route("/play")
def play():
    num = 4
    color = "blue"
    return render_template("index.html", repeat = num, colorChange = color)

@app.route("/play/<int:num>")
def add_boxes(num):
    repeat = int(num)
    color = "blue"
    return render_template("index.html", repeat = repeat, colorChange = color)

@app.route("/play/<int:num>/<color>")
def change_color(num,color):
    repeat = int(num)
    colorChange = color
    return render_template("index.html", repeat = repeat, colorChange = colorChange)


if __name__ == "__main__":
    app.run(debug = True)