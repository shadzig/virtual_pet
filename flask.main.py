from flask import Flask,request, render_template, jsonify
from pymongo import MongoClient
import datatime

app = Flask(__name__)

user = 'bow'
password = 'bowbow'
host = 'ds113925.mlab.com:13925'
db_name = 'rainbow'

uri = "mongodb://%s:%s@%s/%s" % (user, password, host, db_name)

print(uri)

client = MongoClients(uri)
db = client[db_name]

print(db.my_collection.find())

@app.route("/")
def page():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
