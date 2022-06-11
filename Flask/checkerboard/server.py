from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    columns = 4
    row = 4
    return render_template("index.html", x = columns, y = row)

@app.route("/<num_of_rows>")
def add_rows( num_of_rows ):
    columns = 4
    y = int(num_of_rows)
    return render_template("index.html", x= columns, y = y)

@app.route("/<num_of_rows>/<num_of_col>")
def add_columns ( num_of_rows, num_of_col):
    y = int(num_of_rows)
    x = int(num_of_col)
    return render_template("index.html", y = y, x = x)

# @app.route("/<num_of_rows>/<num_of_col>/<color0>/<color1>")
# def change_colors ( num_of_rows, num_of_col, color0, color1):
#     y = int(num_of_rows)
#     x = int(num_of_col)
#     colorChange0 = color0
#     colorChange1 = color1
#     return render_template("index.html", y = y, x = x , colorChange0 = colorChange0, colorChange1 = colorChange1 )

if __name__ == "__main__":
    app.run(debug= True)