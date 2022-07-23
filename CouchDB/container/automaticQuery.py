from ntpath import join
import requests
import json
import xlsxwriter
import os

ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]

ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

collections = ["embedding_a_in_b", "embedding_b_in_a",  "referencing_a_in_b",  "referencing_b_in_a"]


#TODO 
#non va bene cosi bisogna trasporre la matrice come per mongoDB


workbook = xlsxwriter.Workbook('CouchDBStat.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.set_column(1, 1, 20)
worksheet.set_column(2, 2, 20)
worksheet.set_column(3, 3, 20)
worksheet.set_column(4, 4, 20)

worksheet.write_string('B1', 'embedding_A_in_B', bold)
worksheet.write_string('C1', 'embedding_B_in_A', bold)
worksheet.write_string('D1', 'referencing_A_in_B', bold)
worksheet.write_string('E1', 'referencing_B_in_A', bold)

worksheet.write_string('A2', 'A1', bold)
worksheet.write_string('A3', 'A2', bold)
worksheet.write_string('A4', 'A3', bold)
worksheet.write_string('A5', 'A4', bold)
worksheet.write_string('A6', 'A5', bold)
worksheet.write_string('A7', 'A6', bold)
worksheet.write_string('A8', 'B1', bold)
worksheet.write_string('A9', 'B2', bold)
worksheet.write_string('A10', 'B3', bold)
worksheet.write_string('A11', 'B4', bold)
worksheet.write_string('A12', 'B5', bold)
worksheet.write_string('A13', 'B6', bold)

worksheet.write_string('A14' , 'A1j', bold)
worksheet.write_string('A15' , 'A2j', bold)
worksheet.write_string('A16' , 'A3j', bold)
worksheet.write_string('A17' , 'A4j', bold)
worksheet.write_string('A18' , 'A5j', bold)
worksheet.write_string('A19' , 'A6j', bold)
worksheet.write_string('A20' , 'B1j', bold)
worksheet.write_string('A21' , 'B2j', bold)
worksheet.write_string('A22' , 'B3j', bold)
worksheet.write_string('A23' , 'B4j', bold)
worksheet.write_string('A24' , 'B5j', bold)
worksheet.write_string('A25' , 'B6j', bold)

get_rowNum = {'embedding_a_in_b' : 0,'embedding_b_in_a' : 1,'referencing_b_in_a' : 2,'referencing_a_in_b' : 3}
get_colNum = {
    'A1' : 0,'A2' : 1,'A3' : 2,'A4' : 3, 'A5' : 4, 'A6' : 5, 'B1' : 6,'B2' : 7,'B3' : 8,'B4' : 9, 'B5' : 10, 'B6' : 11, 
    'A1join' : 12,'A2join' : 13,'A3join' : 14,'A4join' : 15, 'A5join' : 16, 'A6join' : 17, 'B1join' : 18,'B2join' : 19,'B3join' : 20,'B4join' : 21, 'B5join' : 22, 'B6join' : 23
}

def queryRun(collection, payload):
  url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"

  time = 0
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  resp = json.loads(response.text)
  time += resp["execution_stats"]['execution_time_ms']
  worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
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
  worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
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
        "_id" : key
      },
      "execution_stats": True
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    print(resp)
    time += resp["execution_stats"]['execution_time_ms']
  worksheet.write(get_rowNum[to_col] + 1, get_colNum[ind] + 1, time)
  print("join time: " )
  print(str(time) + " ms") 

    
if __name__ == "__main__":

  val = "8"

  collection = "referencing_B_in_A"
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
    simpleSelection(collection, ind, val)
      # select A.*, B.*
      # from A join B on (A.AK=B.AK)
      # where Ax='val'

##################### TESTARE ##################################################
# join tra referencing_B_in_A (esterna) e referencing_a_in_B (interna)
  url = "http://admin:admin@127.0.0.1:5984/" + "referencing_b_in_a" +"/_find"
  payload = json.dumps({
   "selector": {
      ind : int(val)
   }
   # ,
   # "fields": [
      # "BK",                
      # "B1",
      # "B2",
      # "B3",
      # "B4",
      # "B5",
      # "B6",
      # "B7",
   # ]
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
### qui dovrei prendere le chiavi di AK e per ognuna selezionare il doc di B
  foreign_keys = [list(x.values())[0] for x in resp["docs"]]
  url = "http://admin:admin@127.0.0.1:5984/" + "b" +"/_find"
  for key in foreign_keys:
    payload = json.dumps({
      "selector": {
        "_id" : key
      },
      "execution_stats": True
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    print(resp)
    time += resp["execution_stats"]['execution_time_ms']
  worksheet.write(get_rowNum[to_col] + 1, get_colNum[ind] + 1, time)
  print("join time: " )
  print(str(time) + " ms") 

  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    simpleSelection("b", ind, val)
      # select A.*, B.*
      # from A join B on (A.AK=B.BK)
      # where Bx='val
    url = "http://admin:admin@127.0.0.1:5984/" + "b" +"/_find"
    payload = json.dumps({
    "selector": {
        ind : int(val)
    }
    # ,
    # "fields": [
        # "BK",                
        # "B1",
        # "B2",
        # "B3",
        # "B4",
        # "B5",
        # "B6",
        # "B7",
    # ]
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
##################### TESTARE ##################################################
  ### qui dovrei prendere le chiavi di BK e per ognuna selezionare il doc del refBA
    foreign_keys = [list(x.values())[0] for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
    for key in foreign_keys:
      payload = json.dumps({
        "selector": {
          "_id" : key
        },
        "execution_stats": True
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      resp = json.loads(response.text)
      print(resp)
      time += resp["execution_stats"]['execution_time_ms']
    worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
    print("join time: " )
    print(str(time) + " ms") 

  collection = "referencing_A_in_B"
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
    simpleSelection("a", ind, val)
      # select A.*, B.*
      # from A join B on (A.AK=B.AK)
      # where Ax='val'
    url = "http://admin:admin@127.0.0.1:5984/" + "a" +"/_find"
    payload = json.dumps({
    "selector": {
        ind : int(val)
    }
    # ,
    # "fields": [
        # "AK",                
        # "A1",
        # "A2",
        # "A3",
        # "A4",
        # "A5",
        # "A6",
        # "A7",
    # ]
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
##################### TESTARE ##################################################
  ### qui dovrei prendere le chiavi di AK e per ognuna selezionare il doc del refAB
    foreign_keys = [list(x.values())[0] for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
    for key in foreign_keys:
      payload = json.dumps({
        "selector": {
          "_id" : key
        },
        "execution_stats": True
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      resp = json.loads(response.text)
      print(resp)
      time += resp["execution_stats"]['execution_time_ms']
    worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
    print("join time: " )
    print(str(time) + " ms") 
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    simpleSelection(collection, ind, val)
      # select A.*, B.*
      # from A join B on (A.AK=B.BK)
      # where Bx='val
  ##################### TESTARE ##################################################
  # join tra referencing_A_in_B (esterna) e A (interna)
    url = "http://admin:admin@127.0.0.1:5984/" + "referencing_a_in_b" +"/_find"
    payload = json.dumps({
    "selector": {
        ind : int(val)
    },
      "execution_stats": True
      })
    headers = {
      'Content-Type': 'application/json'
    }
    time = 0
    response = requests.request("POST", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    time += resp["execution_stats"]['execution_time_ms']
  ### qui dovrei prendere le chiavi di AK e per ognuna selezionare il doc di A
    foreign_keys = [list(x.values())[0] for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/" + "a" +"/_find"
    for key in foreign_keys:
      payload = json.dumps({
        "selector": {
          "_id" : key
        },
        "execution_stats": True
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      resp = json.loads(response.text)
      print(resp)
      time += resp["execution_stats"]['execution_time_ms']
    worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
    print("join time: " )
    print(str(time) + " ms")
############################# FINIRE CON EMBEDDING ##################






  exit(0)
  for ind in ind_a:
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
  
  for ind in ind_b:
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
