#mongoimport --collection embedding_A_in_B --db tirocinio  --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --host=localhost:27017 --authenticationDatabase admin  /home/data/embedding_A_in_B.json
#
#
#mongoimport --collection embedding_B_in_A --db tirocinio  --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --host=localhost:27017 --authenticationDatabase admin  /home/data/embedding_B_in_A.json
#
#mongoimport --collection referencing_A_in_B --db tirocinio  --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --host=localhost:27017 --authenticationDatabase admin  /home/data/referencing_A_in_B.json
#
#mongoimport --collection referencing_B_in_A --db tirocinio  --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --host=localhost:27017 --authenticationDatabase admin  /home/data/referencing_B_in_A.json



mongoimport --collection A --db tirocinio  -u root -p pass12345 --host=localhost:27017 --authenticationDatabase admin  /home/data/A.json

mongoimport --collection B --db tirocinio  -u root -p pass12345 --host=localhost:27017 --authenticationDatabase admin  /home/data/B.json

mongoimport --collection embedding_A_in_B --db tirocinio  -u root -p pass12345 --host=localhost:27017 --authenticationDatabase admin  /home/data/embedding_A_in_B.json

mongoimport --collection embedding_B_in_A --db tirocinio  -u root -p pass12345 --host=localhost:27017 --authenticationDatabase admin  /home/data/embedding_B_in_A.json

mongoimport --collection referencing_A_in_B --db tirocinio  -u root -p pass12345 --host=localhost:27017 --authenticationDatabase admin  /home/data/referencing_A_in_B.json

mongoimport --collection referencing_B_in_A --db tirocinio  -u root -p pass12345 --host=localhost:27017 --authenticationDatabase admin  /home/data/referencing_B_in_A.json


