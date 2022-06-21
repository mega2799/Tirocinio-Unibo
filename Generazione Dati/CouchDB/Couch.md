# CouchDB

```sh
cat comment.json | lwp-request -m POST -Ss "http://???:????@127.0.0.1:5984/social" -c "application/json"
```


import couchdb
import json

couch = couchdb.Server("http://????:?????@127.0.0.1:5984")
db = couch.create("social3")
with open("comment.json") as jsonfile:
    for row in jsonfile:
        db_entry = json.loads(row) 
        db.save(db_entry)