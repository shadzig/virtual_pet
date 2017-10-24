from credentials import db_access

host= "ds113925.mlab.com:13925"
db_name = "bow"

uri = "mongodb://%s:%s@%s/%s" % (db_access.user, db_access.passowrd, host, db_name)

print (uri)

client = MongoClient(uri)
db = client[db_name]

post = {"author": "mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymonogo"],
        "data": datetime.datetime.utcnow()}

collection + db.my.posts
collection.insert._one(posts)

for x in db.my_posts.find():
    print(x)
    
