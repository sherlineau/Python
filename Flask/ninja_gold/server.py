from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
app.secret_key = b'\xaf0\xa1\xee\xf6\xa7*\n\x06\x80\xb1\x01\x14~\xb2S'

@app.route("/")
def home():
    if 'gold' in session:
        session['gold'] = session['gold']
    else:
        session['gold'] = 0
    if 'message' in session:
        session['message'] = session['message']   
    else:
        session['message'] = []
    if 'color' in session:
        session['color'] = session['color']   
    else:
        session['color'] = []

    return render_template("index.html", gold = session['gold'], message = session['message'], num = session['color'], )

@app.route("/process_money", methods=["POST"])
def process_money():

    if request.form['building'] == 'farm':
        gold = randint(10,20)
        session['gold'] += gold
        session['message'].insert(0,(f'<p class="my-0" style="color: green">Earned {gold} from the farm!</p>'))
    elif request.form['building'] == 'cave':
        gold = randint(5,10)
        session['gold'] += gold
        session['message'].insert(0,(f'<p class="my-0" style="color: green">Earned {gold} from the cave!</p>'))

    elif request.form['building'] == 'house':
        gold = randint(2,5)
        session['gold'] += gold
        session['message'].insert(0,(f'<p class="my-0" style="color: green">Earned {gold} from the house!</p>'))

    elif request.form['building'] == 'casino':
        gold = randint(-50,50)
        if gold < 0:
            session['message'].insert(0,(f'<p class="my-0" style="color: red">Entered a casino and lost {gold}... Ouch!</p>'))
        else: 
            session['message'].insert(0,(f'<p class="my-0" style="color: green">Earned {gold} from the casino!</p>'))

        session['gold'] += gold
    return redirect('/')    

@app.route("/reset" , methods = ["POST"])
def reset():
    session.clear()
    return redirect("/")
    
    
if __name__ == "__main__":
    app.run(debug=True)