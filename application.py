from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "teste2"


app.run(host='0.0.0.0', debug=True)