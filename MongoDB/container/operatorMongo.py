import pymongo
import json


ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]
ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

collections = ["embedding_A_in_B", "embedding_B_in_A",  "referencing_A_in_B",  "referencing_B_in_A"]



def simple_aggregate(collection ,query):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    return mydb.command(
    {
        'aggregate': collection, 
        'pipeline': query, 
        'cursor': {}
    })

def explain_plan(collection, query):
    #return mydb.command('aggregate', 'embedding_B_in_A', pipeline=query, explain=True)
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    return mydb.command(
        'explain', 
        {
            'aggregate': collection, 
            'pipeline': query, 
            'cursor': {}
        }
    )


def exec_cost(collection, query):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    return mydb.command(
        'explain', 
        {
            'aggregate': collection, 
            'pipeline': query, 
            'cursor': {}
        }, 
        verbosity='executionStats'
    ) 

if __name__ == "__main__":
    print("On which collection should i run the query")
    n = int(input("0)embedding_A_in_B.json\n1)embedding_B_in_A.json\n2)referencing_A_in_B.json\n3)referencing_B_in_A.json\n\n"))

    collection = collections[n]

    if n%2 == 1:
        print("On which index should i run the query")
        i = input("0)A1 \n1)A2 \n2)A3 \n3)A4 \n4)A5 \n5)A6\n\n")
        ind = ind_a[int(i)]
    else:
        print("On which index should i run the query")
        i = input("0)B1 \n1)B2 \n2)B3 \n3)B4 \n4)B5 \n5)B6\n\n")
        ind = ind_b[int(i)]
    
    val = input("On which value?\n\n")

    query = (
        [
            {
                '$match' : { ind : val}
            }
        ]
    )


    print(simple_aggregate(collection, query))

    file = open("result/" + collection + "@" + ind + "exec_stats.json", "w") 

    res = exec_cost(collection, query)

    print(res)

    for l in res:
        print(type(l))

    file.write(json.dumps(res, indent=4))

    file.close()

    file = open("result/" + collection + "@" + ind + "query_plan.json", "w") 

    res = explain_plan(collection, query)

    file.write(json.dumps(res, indent=4))

    file.close()



# database statistics
# print db.command("dbstats")

