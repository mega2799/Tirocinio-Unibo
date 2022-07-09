from ntpath import join
import requests
import json
import os

ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]

ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

collections = ["embedding_a_in_b", "embedding_b_in_a",  "referencing_a_in_b",  "referencing_b_in_a"]


def queryRun(collection, payload):
  url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"

  time = 0
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  resp = json.loads(response.text)
  time += resp["execution_stats"]['execution_time_ms']
  print("sel time: " )
  print(str(time) + " ms") 

def simpleSelection(collection, ind, value):
  url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"

  time = 0

  payload = json.dumps({
    "selector": {
      ind : int(val)
    },
    "execution_stats": True
  })

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  resp = json.loads(response.text)
  time += resp["execution_stats"]['execution_time_ms']
  print("sel time: " )
  print(str(time) + " ms") 

def joinQuery(to_col, from_col, ind, value):
  url = "http://admin:admin@127.0.0.1:5984/" + from_col +"/_find"

  payload = json.dumps({
   "selector": {
      ind : int(val)
   },
   "fields": [
      "AK"
     # ,                da qui prendo solo le chiavi del database esterno per poter calcolare i tempi magari sarebbe da prendere l intero docuemnto
     # "A1",
     # "A2",
     # "A3",
     # "A4",
     # "A5",
     # "A6",
     # "A7",
   ]
   ,
    "execution_stats": True
    })

  headers = {
    'Content-Type': 'application/json'
  }

  time = 0
  response = requests.request("POST", url, headers=headers, data=payload)

  resp = json.loads(response.text)
  time += resp["execution_stats"]['execution_time_ms']
  foreign_keys = [list(x.values())[0] for x in resp["docs"]]
  url = "http://admin:admin@127.0.0.1:5984/" + to_col +"/_find"
  for key in foreign_keys:
    payload = json.dumps({
      "selector": {
        "AK" : key
      },
      "execution_stats": True
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    time += resp["execution_stats"]['execution_time_ms']
  print("join time: " )
  print(str(time) + " ms") 

    
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
    simpleSelection("embedding_b_in_a", ind, val)
    simpleSelection("referencing_b_in_a", ind, val)
    joinQuery("referencing_a_in_b", "referencing_b_in_a", ind, val)

    payload = json.dumps({
      "selector": {
        "A": {
           "$elemMatch": {
              ind : int(val)
         }
      }
     },
      "execution_stats": True
    })

    queryRun("embedding_a_in_b", payload)
  else:
    simpleSelection("embedding_a_in_b", ind, val)
    simpleSelection("referencing_a_in_b", ind, val)
    joinQuery("referencing_b_in_a", "referencing_a_in_b",  ind, val)
    payload = json.dumps({
      "selector": {
        "B": {
           "$elemMatch": {
              ind : int(val)
         }
      }
     },
      "execution_stats": True
    })

    queryRun("embedding_b_in_a", payload)
