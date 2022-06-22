from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'\x94\xc1H\xac\xb6\x9f\xf9z\xc7\xf0cC\xec\xfcLn'

DATABASE = 'emails_schema'