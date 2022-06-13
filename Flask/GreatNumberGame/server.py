from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = b'"\x1fF@\x93&\xad\x83*\xdb\x92\xe9\r\x1e\xe2\xa2'

@app.route("/")
@app.route("/home")
def home():
    # number = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def got_guess():
    session['guess'] = request.form['guess']
    return redirect("/answer")
    
@app.route("/answer")
def show_answer():
    number = random.randint(1,10)
    if int(session['guess']) == number:
        guess = True
    else:
        guess = False
    return render_template("answer.html", guess = guess )

if __name__ == "__main__":
    app.run(debug=True)