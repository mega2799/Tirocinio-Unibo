# CouchDB

```sh
cat comment.json | lwp-request -m POST -Ss "http://???:????@127.0.0.1:5984/social" -c "application/json"
```

Query su couchDb ma non utilizza indici

```json
{
   "selector": {
      "A.A4": 94
   }
}


 "dbname": "social",
 "index": {
  "ddoc": null,
  "name": "_all_docs",
  "type": "special",
  "def": {
   "fields": [
    {
     "_id": "asc"
    }
   ]
  }
 },
 "partitioned": "undefined",
 "selector": {
  "A.A4": {
   "$eq": 94
  }
 },
 "opts": {
  "use_index": [],
  "bookmark": "nil",
  "limit": 25,
  "skip": 0,
  "sort": {},
  "fields": "all_fields",
  "partition": "",
  "r": [
   49
  ],
  "conflicts": false,
  "stale": false,
  "update": true,
  "stable": false,
  "execution_stats": false
 },
 "limit": 25,
 "skip": 0,
 "fields": "all_fields",
 "mrargs": {
  "include_docs": true,
  "view_type": "map",
  "reduce": false,
  "partition": null,
  "start_key": null,
  "end_key": "<MAX>",
  "direction": "fwd",
  "stable": false,
  "update": true,
  "conflicts": "undefined"
 }
}
```

credo che vadano creati
