#!/bin/bash

COLLECTIONS=("embedding_A_in_B"  "embedding_B_in_A"  "referencing_A_in_B"  "referencing_B_in_A");
INDEXESA=("A1"  "A2" "A3"  "A4"  "A5" "A6" )
INDEXESB=("B1"  "B2" "B3"  "B4"  "B5" "B6" )

echo "On which collection should i run the query" 
echo -e "0)embedding_A_in_B.json\n1)embedding_B_in_A.json\n2)referencing_A_in_B.json\n3)referencing_B_in_A.json\t"
read n
col=${COLLECTIONS[${n}]}

if [ $((n%2)) -eq 1 ]
then
	echo "On which index should i run the query" 
	echo -e "0)A1 \n1)A2 \n2)A3 \n3)A4 \n4)A5 \n5)A6"
	read i
	ind=${INDEXESA[${i}]}
else 
	echo "On which index should i run the query" 
	echo -e "0)B1 \n1)B2 \n2)B3 \n3)B4 \n4)B5 \n5)B6"
	read i
	ind=${INDEXESB[${i}]}
fi

echo "Which value ?" 
read v


echo -e "use('tirocinio')"												>> "queries/on_"${col}"ind_"${ind}".js" 
echo -e "printjson(db.getCollection('$col').explain('queryPlanner').aggregate([ { \$match: { \"$ind\" : $v}}]))"  	>> "queries/on_"${col}"ind_"${ind}".js"
echo -e "printjson(db.getCollection('$col').explain('executionStats').aggregate([ { \$match: { \"$ind\" : $v}}]))" 	>> "queries/on_"${col}"ind_"${ind}".js"	

docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/on_"${col}"ind_"${ind}".js" >> "./result/on_"${col}"ind_"${ind}"_Result.json"
