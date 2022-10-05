cat dataJSON/embedding_A_in_B.json  | sed -r 's/"_id":([0-9]+)/ "_id": "\1" /' >> dataCouchDB/embedding_A_in_B.json
cat dataJSON/embedding_B_in_A.json |  sed -r 's/"_id":([0-9]+)/ "_id": "\1" /'  >> dataCouchDB/embedding_B_in_A.json
cat dataJSON/referencing_A_in_B.json| sed -r 's/"_id":([0-9]+)/ "_id": "\1" /' >> dataCouchDB/referencing_A_in_B.json
cat dataJSON/referencing_B_in_A.json| sed -r 's/"_id":([0-9]+)/ "_id": "\1" /' >> dataCouchDB/referencing_B_in_A.json