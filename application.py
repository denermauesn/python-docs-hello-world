from flask import Flask
from validate_docbr import CPF

app = Flask(__name__)

@app.route("/")
def hello():
    return "teste3"

@app.route("/cpfValidator/<cpf>")
def cpfValidator(cpf):
    return str(CPF().validate(cpf))
