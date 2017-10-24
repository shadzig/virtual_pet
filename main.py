from flask import Flask,request, render_template, jsonify
import datetime
import os

ON_HEROKU = "ON_HEROKU" in os.environ

app = Flask(__name__)

@app.route("/")
def page():
    return "Hello World"

if (not ON_HEROKU) and __name__=="__main__":
    app.run(debug=True)
