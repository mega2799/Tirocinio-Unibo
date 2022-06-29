# Passi da ripercorrere e poi scrivere in tesi


`docker pull couchdb` per prelevare l'immagine
`docker run couchdb` per creare il container ma ho errore in cui devo impostare sia utente che password, uso un comando per poter runnare un comando appena il container viene creato oppure uso .yml, magari potrei limitare le risorse con la seconda. 

`winpty docker run -it -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin --name couchDbServer couchdb`  crea un immagine che da errori perche non esiste un db [file](./errorAfterCreating.log)


Provero con il .yml e il compose, magari condividendo i file di configurazione dal SO host


# docker compose 

[info su memoria](https://linuxhint.com/docker_compose_memory_limits/)

[tutti i parametri di compose](https://docs.docker.com/compose/compose-file/)

Comando per poter visualizzare tutte le info
> docker stats --all

# Linux <3 

Installare couchDb server

Stoppare il server con il comando 
> $ sudo systemctl stop couchdb

Avviare il container con il compose nella directory con il comando:
> docker-compose up -d

Entrare all interno del docker con il comando:
> $ docker exec -it CouchDbServerMega bash
