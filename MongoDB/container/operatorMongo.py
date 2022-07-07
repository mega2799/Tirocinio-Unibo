import pymongo
import json
import time


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
        'cursor': {}, 
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

    print("On which index should i run the query")
    i = input("0)A1 \n1)A2 \n2)A3 \n3)A4 \n4)A5 \n5)A6   None\n\n")
    if i != "None":
        ind = ind_a[int(i)]
    else:
        print("On which index should i run the query")
        i = input("0)B1 \n1)B2 \n2)B3 \n3)B4 \n4)B5 \n5)B6\n\n")
        ind = ind_b[int(i)]
    
    print(ind)
    val = input("On which value?\n\n")
    
    if ind in ind_a:
        query = (
            [
                {
                    '$match' : { ind : val}
                }
            ]
        )

        for collection in ["embedding_B_in_A",  "referencing_B_in_A"]:
            start_time = time.time()
            res = simple_aggregate(collection, query)
            file = open("result/" + collection + "@" + ind + "exec_stats.json", "w") 
            print("--- %s seconds ---" % (time.time() - start_time))
            file.write(json.dumps(res, indent=4))

        query = (
            [
                {

                }
            ]
        )
        for collection in ["embedding_A_in_B",  "referencing_B_in_A"]:
            start_time = time.time()
            res = simple_aggregate(collection, query)
            file = open("result/" + collection + "@" + ind + "exec_stats.json", "w") 
            print("--- %s seconds ---" % (time.time() - start_time))
            file.write(json.dumps(res, indent=4))




    exit(0)

    res = exec_cost(collection, query)


    print(res)

    for l in res:
        print(type(l))

    file.write(json.dumps(res, indent=4))

    file.close()

    file = open("result/" + collection + "@" + ind + "query_plan.json", "w") 

    start_time = time.time()

    res = explain_plan(collection, query)

    print("--- %s seconds ---" % (time.time() - start_time))

    file.write(json.dumps(res, indent=4))

    file.close()



# database statistics
# print db.command("dbstats")

