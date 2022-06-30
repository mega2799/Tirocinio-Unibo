mongoexport  --db tirocinio --collection embedding_A_in_B  | sed '/"_id":/s/"_id":[^,]*,//' > container/mongodb-data/embedding_A_in_B.json
mongoexport  --db tirocinio --collection embedding_B_in_A | sed '/"_id":/s/"_id":[^,]*,//' > container/mongodb-data/embedding_B_in_A.json
mongoexport  --db tirocinio --collection referencing_B_in_A | sed '/"_id":/s/"_id":[^,]*,//' > container/mongodb-data/referencing_B_in_A.json
mongoexport  --db tirocinio --collection referencing_A_in_B  | sed '/"_id":/s/"_id":[^,]*,//' > container/mongodb-data/referencing_A_in_B.json
