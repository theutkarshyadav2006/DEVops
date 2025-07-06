from flask import Flask
app = Flask(__name__)

@app.route("/info)
def lwinfo():
	return " i am lucky from sikar"

@app.route("/phone")
def lwphone():
	return "786766767"
app.run(host="0.0.0.0")