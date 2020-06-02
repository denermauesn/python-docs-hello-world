from flask import Flask
from docs_validator import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "teste3"

@app.route("/cpfValidator/<cpf>")
def cpfValidator(cpf):
    return cpf_validator(cpf)