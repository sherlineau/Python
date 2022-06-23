from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'\xa4~\xa8\ns\x9b\xa1@\xe6\xaa\xec\xfcz*\x8d\xca'

DATABASE = 'registration_schema'