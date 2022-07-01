# MongoDb

Stesso procedimento usato per couch con docker-compose.yml

I dati generati in formato JSON dovrebbero essere condivisi al container, devo trovare un modo per poter eseguire script di importazione/esecusione di queries e simili


Con il command CMD ["sh", "/path/to/file.sh"]


comando per importare da dentro container
> mongoimport --collection embedding_A_in_B --db tirocinio  --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --host=localhost:27017 --authenticationDatabase admin  /home/data/embedding_A_in_B.json



alla fine per importare ho fatto uno script che instanzia il container, aspetta e poi importa i files

comando per caricare i file con mongosh 
> mongosh -u root -p pass12345 --authenticationDatabase admin

verra usato per creare gli indici e poi chissà
