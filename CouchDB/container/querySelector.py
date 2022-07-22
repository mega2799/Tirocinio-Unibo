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
worksheet.set_column(0, 0, 20)
worksheet.write_string('A2', 'embedding_A_in_B', bold)
worksheet.write_string('A3', 'embedding_B_in_A', bold)
worksheet.write_string('A4', 'referencing_A_in_B', bold)
worksheet.write_string('A5', 'referencing_A_in_B', bold)

worksheet.write_string('B1', 'A1', bold)
worksheet.write_string('C1', 'A2', bold)
worksheet.write_string('D1', 'A3', bold)
worksheet.write_string('E1', 'A4', bold)
worksheet.write_string('F1', 'A5', bold)
worksheet.write_string('G1', 'A6', bold)
worksheet.write_string('H1', 'B1', bold)
worksheet.write_string('I1', 'B2', bold)
worksheet.write_string('J1', 'B3', bold)
worksheet.write_string('K1', 'B4', bold)
worksheet.write_string('L1', 'B5', bold)
worksheet.write_string('M1', 'B6', bold)

get_rowNum = {'embedding_a_in_b' : 0,'embedding_b_in_a' : 1,'referencing_b_in_a' : 2,'referencing_a_in_b' : 3}
get_colNum = {'A1' : 0,'A2' : 1,'A3' : 2,'A4' : 3, 'A5' : 4, 'A6' : 5, 'B1' : 6,'B2' : 7,'B3' : 8,'B4' : 9, 'B5' : 10, 'B6' : 11}

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
  joinQuery("referencing_a_in_b", "referencing_b_in_a", "A6", val)
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
