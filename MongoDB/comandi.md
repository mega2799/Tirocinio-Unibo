# Export

 .\mongoexport.exe --collection embedding_A_in_B --db tirocinio --out .\embedding_A_in_B.json

.\mongoexport.exe --collection embedding_B_in_A --db tirocinio --out .\embedding_B_in_A.json

.\mongoexport.exe --collection referencing_B_in_A --db tirocinio --out .\referencing_B_in_A.json

.\mongoexport.exe --collection referencing_A_in_B --db tirocinio --out .\referencing_A_in_B.json

Ma couchDB non accetta che l'id sia trasportato (giustamente) quindi uso bash (quanto e' potente) con sed e risolve

./mongoexport.exe  --db tirocinio --collection embedding_A_in_B  | sed '/"_id":/s/"_id":[^,]*,//' > embedding_A_in_B.json

./mongoexport.exe  --db tirocinio --collection embedding_B_in_A | sed '/"_id":/s/"_id":[^,]*,//' > embedding_B_in_A.json

./mongoexport.exe  --db tirocinio --collection referencing_B_in_A | sed '/"_id":/s/"_id":[^,]*,//' > referencing_B_in_A.json

./mongoexport.exe  --db tirocinio --collection referencing_A_in_B  | sed '/"_id":/s/"_id":[^,]*,//' > referencing_A_in_B.json
