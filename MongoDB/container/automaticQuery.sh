#!/bin/bash

COLLECTIONS=("embedding_A_in_B"  "embedding_B_in_A"  "referencing_A_in_B"  "referencing_B_in_A")
INDEXESA=("A1"  "A2" "A3"  "A4"  "A5" "A6" )
INDEXESB=("B1"  "B2" "B3"  "B4"  "B5" "B6" )

echo "Which value ?" 
read v


for col in "embedding_B_in_A"  "referencing_B_in_A"  
do 
	for ind in "A1"  "A2" "A3"  "A4"  "A5" "A6"
	do
		echo -e "use('tirocinio')"												>> "queries/"${col}"@"${ind}"@query_plan.js" 
		echo -e "print(EJSON.stringify(db.getCollection('$col').explain('queryPlanner').aggregate([ { \$match: { \"$ind\" : $v}}]), null, \"  \")"  	>> "queries/"${col}"@"${ind}"@query_plan.js" 
		
		echo -e "use('tirocinio')"												>> "queries/"${col}"@"${ind}"@exec_stats.js"	
		echo -e "print(EJSON.stringify(db.getCollection('$col').explain('executionStats').aggregate([ { \$match: { \"$ind\" : $v}}]), null, \" \"))" >> "queries/"${col}"@"${ind}"@exec_stats.js"	

	
		docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/"${col}"@"${ind}"@query_plan.js" | sed 1,25d >> "./result/"${col}"@"${ind}"@query_plan_Result.json"
		docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/"${col}"@"${ind}"@exec_stats.js" | sed 1,25d >> "./result/"${col}"@"${ind}"@exec_stats_Result.json"
	done
done



for col in "embedding_A_in_B"  "referencing_A_in_B"  
do 
	for ind in "B1"  "B2" "B3"  "B4"  "B5" "B6"
	do
		echo -e "use('tirocinio')"												>> "queries/"${col}"@"${ind}"@query_plan.js" 
		echo -e "print(EJSON.stringify(db.getCollection('$col').explain('queryPlanner').aggregate([ { \$match: { \"$ind\" : $v}}]), null, \"  \")"  	>> "queries/"${col}"@"${ind}"@query_plan.js" 
		
		echo -e "use('tirocinio')"												>> "queries/"${col}"@"${ind}"@exec_stats.js"	
		echo -e "print(EJSON.stringify(db.getCollection('$col').explain('executionStats').aggregate([ { \$match: { \"$ind\" : $v}}]), null, \" \"))" >> "queries/"${col}"@"${ind}"@exec_stats.js"	

	
		docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/"${col}"@"${ind}"@query_plan.js" | sed 1,25d >> "./result/"${col}"@"${ind}"@query_plan_Result.json"
		docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/"${col}"@"${ind}"@exec_stats.js" | sed 1,25d >> "./result/"${col}"@"${ind}"@exec_stats_Result.json"
	done
done


