# Passi da ripercorrere e poi scrivere in tesi


`docker pull couchdb` per prelevare l'immagine
`docker run couchdb` per creare il container ma ho errore in cui devo impostare sia utente che password, uso un comando per poter runnare un comando appena il container viene creato oppure uso .yml, magari potrei limitare le risorse con la seconda. 

`winpty docker run -it -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin --name couchDbServer couchdb`  crea un immagine che da errori perche non esiste un db [file](./errorAfterCreating.log)
