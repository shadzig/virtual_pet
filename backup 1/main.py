from flask import Flask,request, render_template, jsonify, send_from_directory
from pymongo import MongoClient
import datetime
import os

from  credentials import db_access

host= "ds113925.mlab.com:13925"
db_name = "rainbow"

uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.password, host, db_name)

print (uri)

client = MongoClient(uri)
db = client[db_name]

for x in db.my.posts.find():
    print(x)


ON_HEROKU = "ON_HEROKU" in os.environ

app = Flask(__name__)

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("js", path)

@app.route("/")
def page():
    return render_template("index.html", data=db.my_posts.find())

if (not ON_HEROKU) and __name__=="__main__":
    app.run(debug=True)
