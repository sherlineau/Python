from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/display')
def show_emails():
    return render_template("success.html", emails = Email.get_all())


@app.route('/register', methods=['POST'])
def register_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    else:
        # get one
        if Email.get_one({'email':request.form['email']}):
            flash("This email has already been used!")
            return redirect('/')
        else:
            Email.save(request.form)
            return redirect("/display")

    
    

    