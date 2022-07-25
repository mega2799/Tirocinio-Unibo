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

{
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

# indici

documentazione [here](https://docs.couchdb.org/en/latest/api/database/find.html#post--db-_index)

tramite postman sono in grado di effettuare delle query con l'uso di POST e GET

esiste l'immagine su docker hub di [couchDB](https://hub.docker.com/_/couchdb), in questo modo si potrebbe poter limitare l'uso di cache (?)
attraverso docker potrebbe essere facile poter creare un cluster.




## NO CACHE 

 docker-compose rm --all &&
 docker-compose pull &&
 docker-compose build --no-cache &&
 docker-compose up -d --force-recreate 
