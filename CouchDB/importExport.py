import couchdb
import json
from tqdm import tqdm

couch = couchdb.Server("http://admin:admin@127.0.0.1:5984")

db = couch.create("a")

with open("A.json") as jsonfile:
        for row in tqdm(jsonfile):
            db_entry = json.loads(row) 
            db.save(db_entry)

db = couch.create("b")

with open("B.json") as jsonfile:
        for row in tqdm(jsonfile):
            db_entry = json.loads(row) 
            db.save(db_entry)

try:
    db = couch.create("referencing_a_in_b")
    with open("referencing_A_in_B.json") as jsonfile:
        for row in tqdm(jsonfile):
            db_entry = json.loads(row) 
            db.save(db_entry)

    db = couch.create("referencing_b_in_a")
    with open("referencing_B_in_A.json") as jsonfile:
        for row in tqdm(jsonfile):
            db_entry = json.loads(row) 
            db.save(db_entry)
except IOError:
    print("No documents found")

try:
    db = couch.create("embedding_a_in_b")
    with open("embedding_A_in_B.json") as jsonfile:
        for row in tqdm(jsonfile):
            db_entry = json.loads(row) 
            db.save(db_entry)
except IOError:
    print("No redunant document found")

try:
    db = couch.create("embedding_b_in_a")
    with open("embedding_B_in_A.json") as jsonfile:
        for row in tqdm(jsonfile):
            db_entry = json.loads(row) 
            db.save(db_entry)
except IOError:
    print("No redunant document found")