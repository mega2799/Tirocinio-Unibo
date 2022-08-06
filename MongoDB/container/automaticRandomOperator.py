from random import randint
import pymongo
import json
import time


expA = 5

expB = 6

N_A = 10**expA 

N_B = 10**expB

N_A1 = N_A/10

N_A2 = N_A/10**(round(expA/2))

N_A3 = N_A/10**(expA - 1)

N_B1 = N_B/10

N_B2 = N_B/10**(round(expB/2))

N_B3 = N_B/10**(expB - 1)


ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]
ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

collections = ["embedding_A_in_B", "embedding_B_in_A",  "referencing_A_in_B",  "referencing_B_in_A"]

def get_random_indexed_int_A(ind):
  if "1" in ind or "4" in ind :
    return randint(0, N_A1 - 1)
  elif "2" in ind or "5" in ind:
    return randint(0, N_A2 - 1)
  elif "3" in ind or "6" in ind:
    return randint(0, N_A3 - 1)

def get_random_indexed_int_B(ind):
  if "1" in ind or "4" in ind :
    return randint(0, N_B1 - 1)
  elif "2" in ind or "5" in ind:
    return randint(0, N_B2 - 1)
  elif "3" in ind or "6" in ind:
    return randint(0, N_B3 - 1)

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


def exec_cost_once(collection, query):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    print("plan", query)
    return mydb.command(
        'explain', 
        {
            'aggregate': collection, 
            'pipeline': query, 
            'cursor': {}
        }, 
        verbosity='executionStats'
    ) 

def exec_cost(collection, query):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    print("plan", query)
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

    collection = "referencing_B_in_A"
    #key 
    query = ([
  {
    '$match' : {
      "_id" : 5192 
    }
  }
  ])  
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    # foreign key 
    query = ([
  {
    '$match': {
      "B" : {
        "$elemMatch" : {"$eq" : 5192}
      }
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #join on PK 
    query = ([
  {
    '$unwind': {
      'path': "$B",
    }
  },{
    '$lookup': {
      'from': 'B',
      'localField': 'B',
      'foreignField': 'BK',
      'as': 'B'
    }
  },{
    '$match': {
      "_id" : 5192 
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #join on FK 
    query = ([
  {
    '$match': {
      "BK" : 5192
    }
  },
  {
    '$lookup': {
      'from': 'referencing_B_in_A',
      'localField': 'BK',
      'foreignField': 'BK',
      'as': 'B'
    }
  }
])
    start_time = time.time()
    res = exec_cost("B", query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = (
                [
                    {
                        '$match' : { ind : get_random_indexed_int_A(ind)}
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
        query = ([{'$match' : { ind : get_random_indexed_int_A(ind)} }, {'$unwind' : {  'path': "$B"}}, {
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
                    '$match' : { ind : get_random_indexed_int_B(ind)}
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
            ind : get_random_indexed_int_B(ind)
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
    #key 
    query = ([
  {
    '$match' : {
      "_id" : 5192 
    }
  }
])  
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #foreign key 
    query = ([
  {
    '$match': {
      "AK" : 5192
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #join on PK 
    query = ([
  {
    '$unwind': {
      'path': "$A",
    }
  },{
    '$lookup': {
      'from': 'Ap',
      'localField': 'AK',
      'foreignField': 'AK',
      'as': 'A'
    }
  },{
    '$match': {
      "_id" : 5192 
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #join on FK 
    query = ([
  {
    '$match': {
      "AK" : 5192
    }
  },{
    '$lookup': {
      'from': 'referencing_A_in_B',
      'localField': 'AK',
      'foreignField': 'AK',
      'as': 'A'
    }
  }
])
    start_time = time.time()
    res = exec_cost("Ap", query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = (
                [
                    {
                        '$match' : { ind : get_random_indexed_int_A(ind)}
                    }
                ]
            )
        start_time = time.time()
        res = exec_cost("Ap", query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query = ([{'$match' : { ind  : get_random_indexed_int_A(ind) } }, {'$unwind': {  'path': "$B"}},{'$lookup': {'from': 'referencing_A_in_B','localField': 'B','foreignField': 'BK','as': 'B'}}])
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
        res = exec_cost("referencing_B_in_A", query)
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
                    '$match' : { ind : get_random_indexed_int_B(ind)}
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
        query = ([{'$match' : {ind : get_random_indexed_int_B(ind)}},{
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
    #key 
    query = ([
  {
    '$match': {
      "_id" : 5192 
    }
  },{
    '$project': {
      "A" : 0
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #foreign key 
    query = ([
  {
    '$match': {
      "B.BK" : 5192 
    }
  },{
  '$project': {
    "B" : 1
  }}
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #join on PK 
    query = ([
  {
    '$match': {
      "_id" : 5192 
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #join on FK 
    query = ([
  {
    '$match': {
      "B.BK" : 5192 
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = (
                [
                    {
                        '$match' : { ind : get_random_indexed_int_A(ind)}
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
                        '$match' : { ind : get_random_indexed_int_A(ind)}
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
        val = get_random_indexed_int_B(ind)
        query = ([{'$match': {"B." + ind : val}},{'$unwind': {'path' : "$B"}},{'$match' : {"B." + ind : val}}, {'$project':{"B" : 1, "_id" : 0}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        val = get_random_indexed_int_B(ind)
        query = ([{'$match': {"B." + ind : val}},{'$unwind': {'path' : "$B"}},{'$match' : {"B." + ind : val}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))

    collection = "embedding_A_in_B"
    #key 
    query = ([
  {
    '$match': {
      "_id" : 5192 
    }
  },{
    '$project': {
      "B" : 0
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    #foreign key 
    query = ([
  {
    '$match': {
      "A.AK" : 5192 
    }
  },{
  '$project': {
    "A" : 1
  }}
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    # join on PK 
    query = ([
  {
    '$match': {
      "_id" : 5192 
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "B0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    # join on FK 
    query = ([
  {
    '$match': {
      "A.AK" : 5192 
    }
  }
])
    start_time = time.time()
    res = exec_cost(collection, query)
    print("--- %s seconds ---" % (time.time() - start_time))
    file = open("result/" + collection + "@" + "A0join" + "@exec_stats.json", "w") 
    file.write(json.dumps(res, indent=4))
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        query = ([{'$match': {"A." + ind : get_random_indexed_int_A(ind)}},{'$project': {"A" : 1, "_id" : 0}},{'$unwind' : {'path' : "$A"}}])
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query = ([{'$match': {"A." + ind : get_random_indexed_int_A(ind)}}])
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
                        '$match' : { ind : get_random_indexed_int_B(ind)}
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
                        '$match' : { ind : get_random_indexed_int_B(ind)}
                    }
                ]
            )
        start_time = time.time()
        res = exec_cost(collection, query)
        print("--- %s seconds ---" % (time.time() - start_time))
        file = open("result/" + collection + "@" + ind + "join" + "@exec_stats.json", "w") 
        file.write(json.dumps(res, indent=4))