from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = b'tQC"\x05:\x85\xaaW\xc1\xc3}J\xc6\xfd\xff'

@app.route('/', methods= ['GET','POST'])
@app.route('/counter', methods= ['GET','POST'])
def counter():
    if 'count' not in session:
        session['count'] = 1
    if request.method == 'POST':
        if request.form.get('increment') == 'add one':
            session['count'] += 1
        elif request.form.get('addtwo') == 'add two':
            session['count'] += 2
        elif request.form.get('reset') == 'reset':
            session['count'] = 1
        else: 
            pass
    elif request.method == 'GET':
        return render_template('index.html',  count = session['count'])
    
    return render_template("index.html" , count = session['count'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)