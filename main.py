from flask import Flask,request, render_template, jsonify
import datatime

LOCAL = False

app = Flask(__name__)

@app.route("/")
def page():
    return "Hello World"

if LOCAL and __name__=="__main__":
    app.run(debug=True)
