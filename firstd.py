from flask import Flask
app = Flask(__name__)

@app.route("/info)
def lwinfo():
	return " i am UTKARSH YADAV"

@app.route("/phone")
def lwphone():
	return "88888888"
app.run(host="0.0.0.0")
