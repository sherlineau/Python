from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = b'\xa2\xbf\x7f:\x16\xdf4\x1d[\x93)T\x99q\x0cE'
# good secret keys can be generated using python command
# python -c 'import os; pring(os.urandom(16))'
# outputs random byte string

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods = ['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # never render template when using POST method
    # always redirect
    return redirect('/show')

#to get post information to show up on redirected page
#need to use SESSIONS
#sessins need to have a app.secret_key 
@app.route('/show')
def show_user():
    return render_template("show.html", name_on_template = session['username'], email_on_template= session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)