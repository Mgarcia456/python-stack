from flask import Flask
app = Flask(__name__)
app.secret_key = "hiddenkey"
DATABASE = 'dojos_and_ninjas'