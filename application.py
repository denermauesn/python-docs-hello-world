from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "teste3"

@app.route("/novo")
def novo():
    return "novo"