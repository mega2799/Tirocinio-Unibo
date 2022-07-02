#!/bin/bash

COLLECTIONS=( "referencing_B_in_A" "referencing_A_in_B"  );
INDEXESA=("A1"  "A2" "A3"  "A4"  "A5" "A6" )
INDEXESB=("B1"  "B2" "B3"  "B4"  "B5" "B6" )

echo "On which collection should i run the join query? " 
echo -e "0) A as attribute \n1)B as attribute"
read n
col=${COLLECTIONS[${n}]}

if [ $((n%2)) -eq 0 ]
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


echo -e "use('tirocinio')"												>> "queries/join_on_"${col}"ind_"${ind}"_query_plan.js" 
echo -e "use('tirocinio')"												>> "queries/join_on_"${col}"ind_"${ind}"_exec_stats.js" 
echo -e "printjson(db.getCollection('$col').explain('queryPlanner').aggregate([ { \$match: { \"${ind}\" : ${v} }},{ \$unwind: { path: \"\$B\", } } ,{ \$lookup: { from: 'referencing_A_in_B', localField: 'B', foreignField: 'BK', as: 'B' } } ,{ \$unwind: { path: \"\$B\", } } ,{ \$project : { \"AK\" : \"\$AK\", \"A1\" : \"\$A1\", \"A2\" : \"\$A2\", \"A3\" : \"\$A3\", \"A4\" : \"\$A4\", \"A5\" : \"\$A5\", \"A6\" : \"\$A6\", \"A7\" : \"\$A7\", \"BK\" : \"\$B.AK\", \"B1\" : \"\$B.A1\", \"B2\" : \"\$B.A2\", \"B3\" : \"\$B.A3\", \"B4\" : \"\$B.A4\", \"B5\" : \"\$B.A5\", \"B6\" : \"\$B.A6\", \"B7\" : \"\$B.A7\" } }]))"  	>> "queries/join_on_"${col}"ind_"${ind}"_query_plan.js"

echo -e "printjson(db.getCollection('$col').explain('executionStats').aggregate([ { \$match: { \"${ind}\" : ${v} }},{ \$unwind: { path: \"\$B\", } } ,{ \$lookup: { from: 'referencing_A_in_B', localField: 'B', foreignField: 'BK', as: 'B' } } ,{ \$unwind: { path: \"\$B\", } } ,{ \$project : { \"AK\" : \"\$AK\", \"A1\" : \"\$A1\", \"A2\" : \"\$A2\", \"A3\" : \"\$A3\", \"A4\" : \"\$A4\", \"A5\" : \"\$A5\", \"A6\" : \"\$A6\", \"A7\" : \"\$A7\", \"BK\" : \"\$B.AK\", \"B1\" : \"\$B.A1\", \"B2\" : \"\$B.A2\", \"B3\" : \"\$B.A3\", \"B4\" : \"\$B.A4\", \"B5\" : \"\$B.A5\", \"B6\" : \"\$B.A6\", \"B7\" : \"\$B.A7\" } }]))"  	>> "queries/join_on_"${col}"ind_"${ind}"_exec_stats.js"

#echo -e "docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f \"on_\"${col}\"ind_\"${ind}\".js\"  > /result/\"on_\"${col}\"ind_\"${ind}\"_Result.js"
docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/join_on_"${col}"ind_"${ind}"_query_plan.js" >> "./result/join_on_"${col}"ind_"${ind}"_plan_Result.json"
docker exec -it mongodb mongosh -u root -p pass12345 --authenticationDatabase admin -f "/home/queries/join_on_"${col}"ind_"${ind}"_exec_stats.js" >> "./result/join_on_"${col}"ind_"${ind}"_exec_Result.json"







