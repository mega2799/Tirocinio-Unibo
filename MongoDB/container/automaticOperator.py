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
    print(collection, ind)
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
    val = 8

    collection = "referencing_B_in_A"
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = (
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query = ([{'$match' : { ind : val} }, {'$unwind' : {  'path': "$B"}}, {
        '$lookup': {
        'from': 'B',
        'localField': 'B',
        'foreignField': 'BK',
        'as': 'B'
        }},{'$unwind' : {'path' : "$B"}}, {'$project' : {"B._id" : 0}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        query = (
            [
                {
                    '$match' : { ind : val}
                }
            ]
        )
        start_time = time.time()
        res = exec_cost("B", query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        query = ([{
        '$match': {
            ind : val
        }},{
        '$lookup': {
        'from' : 'referencing_B_in_A',
        'localField' : 'FAK',
        'foreignField' : 'AK',
        'as' : 'A'
        }}, {
        '$project': {
          "_id" : 0,
          "FAK" : 0,
          "A.B" : 0
        }},{'$unwind' : {'path' : "$A"}}])
        start_time = time.time()
        res = exec_cost("B", query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))

    collection = "referencing_A_in_B"
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = (
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )
        start_time = time.time()
        res = exec_cost("A", query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query = ([{'$match' : { ind  : val } },{'$lookup': {'from': 'referencing_A_in_B','localField': 'AK','foreignField': 'BK','as': 'B'}},{'$unwind': {'path': "$B"}},{'$project' : {"_id" : 0, "B._id" : 0}}])
       # query = ([{
       #     '$match': {
       #         ind : val
       #     }},{
       #     '$lookup': {
       #     'from': 'referencing_A_in_B',
       #     'localField' : 'AK',
       #     'foreignField' : 'AK',
       #     'as': 'B'
       #     }}, {
       #     '$project': {
       #     "_id" : 0
       #     }}])
        start_time = time.time()
        res = exec_cost("A", query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        query = (
            [
                {
                    '$match' : { ind : val}
                }
            ]
        )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        query = ([{'$match' : {ind : val}},{
            '$lookup': {
            'from': 'A',
            'localField': 'AK',
            'foreignField': 'AK',
            'as': 'A'
            }},{
            '$project': {
            "A._id" : 0
            }},{'$unwind' : {'path': "$A"}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))

    collection = "embedding_B_in_A"
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = (
                [
                    {
                        '$match' : { ind : val}
                    },{ '$project' : { "B" : 0}}
                ]
            )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query =(
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        query = ([{'$match': {"B." + ind : val}},{'$unwind': {'path' : "$B"}},{'$match' : {"B." + ind : val}}, {'$project':{"B" : 1, "_id" : 0}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        query = ([{'$match': {"B." + ind : val}},{'$unwind': {'path' : "$B"}},{'$match' : {"B." + ind : val}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))

    collection = "embedding_A_in_B"
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = ([{'$match': {"A." + ind : val}},{'$project': {"A" : 1, "_id" : 0}},{'$unwind' : {'path' : "$A"}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query = ([{'$match': {"A." + ind : val}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        query =(
                [
                    {
                        '$match' : { ind : val}
                    },{ '$project' : { "A" : 0}}
                ]
            )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        query = (
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))