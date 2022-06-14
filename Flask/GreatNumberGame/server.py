from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = b'"\x1fF@\x93&\xad\x83*\xdb\x92\xe9\r\x1e\xe2\xa2'

@app.route("/")
@app.route("/home")
def home():
    session['number'] = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def got_guess():
    session['guess'] = request.form['guess']
    return redirect("/answer")
    
@app.route("/answer")
def show_answer():
    # number = session['number']
    if int(session['guess']) == session['number']:
        guess = True
        return render_template("answer.html", guess = guess)
    else:
        guess = False
        if int(session['guess']) > session['number']:
            lower = False
        else:
            lower = True
        return render_template("answer.html", guess = guess , lower = lower)

@app.route('/playagain', methods=['POST'])
def play_again():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)