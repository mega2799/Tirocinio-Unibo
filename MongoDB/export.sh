# mongoexport  --db tirocinio --collection embedding_A_in_B  | sed '/"_id":/s/"_id":[^,]*,//' > 	../dataJSON/embedding_A_in_B.json
# mongoexport  --db tirocinio --collection embedding_B_in_A | sed '/"_id":/s/"_id":[^,]*,//' > 	../dataJSON/embedding_B_in_A.json
# mongoexport  --db tirocinio --collection referencing_B_in_A | sed '/"_id":/s/"_id":[^,]*,//' > 	../dataJSON/referencing_B_in_A.json
# mongoexport  --db tirocinio --collection referencing_A_in_B  | sed '/"_id":/s/"_id":[^,]*,//' > ../dataJSON/referencing_A_in_B.json
# mongoexport  --db tirocinio --collection betterA | sed '/"_id":/s/"_id":[^,]*,//' > ../dataJSON/A.json
# mongoexport  --db tirocinio --collection betterB   | sed '/"_id":/s/"_id":[^,]*,//' > ../dataJSON/B.json


mongoexport  --db tirocinio --collection embedding_A_in_B  > 	../dataJSON/embedding_A_in_B.json
mongoexport  --db tirocinio --collection embedding_B_in_A  > 	../dataJSON/embedding_B_in_A.json
mongoexport  --db tirocinio --collection referencing_B_in_A  > 	../dataJSON/referencing_B_in_A.json
mongoexport  --db tirocinio --collection referencing_A_in_B   > ../dataJSON/referencing_A_in_B.json
mongoexport  --db tirocinio --collection A  > ../dataJSON/A.json
mongoexport  --db tirocinio --collection B > ../dataJSON/B.json
