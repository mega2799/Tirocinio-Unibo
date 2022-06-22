import couchdb
import json

couch = couchdb.Server("http://admin:admin@127.0.0.1:5984")
db = couch.create("social")
try:
    with open("post.json") as jsonfile:
        for row in jsonfile:
            db_entry = json.loads(row) 
            db.save(db_entry)

    with open("comment.json") as jsonfile:
        for row in jsonfile:
            db_entry = json.loads(row) 
            db.save(db_entry)
except IOError:
    print("No documents found")

try:
    with open("commentAndPost.json") as jsonfile:
        for row in jsonfile:
            db_entry = json.loads(row) 
            db.save(db_entry)
except IOError:
    print("No redunant document found")

try:
    print("No redunant documents found")
    with open("postAndComment.json") as jsonfile:
        for row in jsonfile:
            db_entry = json.loads(row) 
            db.save(db_entry)
except IOError:
    print("No redunant document found")