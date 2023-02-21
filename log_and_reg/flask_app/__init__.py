from flask import Flask
app = Flask(__name__)
app.secret_key = "hiddenkey"
DATABASE = 'log_and_reg'