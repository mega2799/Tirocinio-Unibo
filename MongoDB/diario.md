# MongoDb

Stesso procedimento usato per couch con docker-compose.yml

I dati generati in formato JSON dovrebbero essere condivisi al container, devo trovare un modo per poter eseguire script di importazione/esecusione di queries e simili

Con il command CMD ["sh", "/path/to/file.sh"]

comando per importare da dentro container
> mongoimport --collection embedding_A_in_B --db tirocinio  --username $MONGO_INITDB_ROOT_USERNAME --password $MONGO_INITDB_ROOT_PASSWORD --host=localhost:27017 --authenticationDatabase admin  /home/data/embedding_A_in_B.json

alla fine per importare ho fatto uno script che instanzia il container, aspetta e poi importa i files

comando per caricare i file con mongosh
> mongosh -u root -p pass12345 --authenticationDatabase admin

verra usato per creare gli indici

query d esempio:

> db.getCollection('embedding_B_in_A').aggregate([ { $match: { "AK" : 99 } }]);

Mi ritorna molte copie dello stesso A, non so perche' !CONTROLLARE!

Query per poter leggere le stats
> db.getCollection('embedding_B_in_A').explain('executionStats').aggregate([ { $match: { "AK" : 99 } }]);

Confermo di ricevere 10 copie dello stesso A.....

Le query vengono eseguite e funzionano perfettamente tranne gli exec cost dei join......

sarebbe il caso di separare i json dell explainPlan e del exex cost in modo da poterli parsare separati

ma ancora ho le prime 25 righe intasate di roba, magari con un sed 1,25d riesco a levare tutto, sarebbe da fare sulla cartella result
