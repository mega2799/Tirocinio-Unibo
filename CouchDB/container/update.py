from random import randint
from ntpath import join
import requests
import json
import xlsxwriter
import numpy as np
import os
import time

expA = 4

expB = 5

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

collections = ["embedding_a_in_b", "embedding_b_in_a",  "referencing_a_in_b",  "referencing_b_in_a"]


workbook = xlsxwriter.Workbook('CouchDBStatUpdate.xlsx')
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

worksheet.write_string('A2', 'A0', bold)
worksheet.write_string('A3', 'A1', bold)
worksheet.write_string('A4', 'A2', bold)
worksheet.write_string('A5', 'A3', bold)
worksheet.write_string('A6', 'A4', bold)
worksheet.write_string('A7', 'A5', bold)
worksheet.write_string('A8', 'A6', bold)
worksheet.write_string('A9', 'B0', bold)
worksheet.write_string('A10', 'B1', bold)
worksheet.write_string('A11', 'B2', bold)
worksheet.write_string('A12', 'B3', bold)
worksheet.write_string('A13', 'B4', bold)
worksheet.write_string('A14', 'B5', bold)
worksheet.write_string('A15', 'B6', bold)

get_rowNum = {'embedding_a_in_b' : 0,'embedding_b_in_a' : 1,'referencing_b_in_a' : 2,'referencing_a_in_b' : 3}
get_colNum = {'A0' : 0,'A1' : 1,'A2' : 2,'A3' : 3,'A4' : 4,'A5' : 5,'A6' : 6,'B0' : 7,'B1' : 8,'B2' : 9,'B3' : 10,'B4' : 11,'B5' : 12,'B6' : 13}


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

def selectAndUpdate(collection, ind, val):
  start_time = time.time()
  url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
  payload = json.dumps({
    "selector": {
      ind : int(val)
    }
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  resp = json.loads(response.text)
  headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
  }

  for doc in resp["docs"]:
    id = doc["_id"]
    url = "http://admin:admin@127.0.0.1:5984/" + collection +"/" + id
    payload = json.dumps(doc)
    response = requests.request("PUT", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    if (resp["ok"] == False):
      print("error")
      exit(0)
    return (time.time() - start_time)
    
def selectAndUpdateEmbedded(collection, payload):
  start_time = time.time()
  url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  resp = json.loads(response.text)
  headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
  }

  for doc in resp["docs"]:
    id = doc["_id"]
    url = "http://admin:admin@127.0.0.1:5984/" + collection +"/" + id
    payload2 = json.dumps(doc)
    response = requests.request("PUT", url, headers=headers, data=payload2)
    resp = json.loads(response.text)
    if (resp["ok"] == False):
      print("error")
      exit(0)
    return (time.time() - start_time) * 1000
    

def refBA():
  collection = "referencing_b_in_a"
  print("i'm in " + collection)
  # key 
  t = selectAndUpdate(collection, "AK", 67)
  worksheet.write( get_colNum["A0"] + 1, get_rowNum[collection] + 1,t)
  print(t)
  # foreign key 
  t = selectAndUpdate("b", "BK", 67)
  worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1,t)
  print(t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
    t = selectAndUpdate(collection, ind, val)
    worksheet.write( get_colNum[ind] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx= vaal
    t = selectAndUpdate("b", ind, val)
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)

def refAB():
  collection = "referencing_a_in_b"
  print("i'm in " + collection)
  # key 
  t = selectAndUpdate(collection, "BK", 67)
  worksheet.write( get_colNum["B0"] + 1, get_rowNum[collection] + 1,t)
  # foreign key 
  t = selectAndUpdate("a", "AK", 67)
  worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
    t = selectAndUpdate("a", ind, val)
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    t = selectAndUpdate(collection, ind, val)
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)

if __name__ == "__main__":

  val = "8"
  refBA()
  refAB()


  collection = "embedding_b_in_a"
  # key 
  t = selectAndUpdate(collection, "AK", 67)
  worksheet.write( get_colNum["A0"] + 1, get_rowNum[collection] + 1,t)
  # foreign key 
  payload = json.dumps({
      "selector": {
          "B_ind": {
            "$elemMatch": {
                "BK" : 67
            }
          }
      }    })
  t = selectAndUpdateEmbedded(collection, payload)
  worksheet.write( get_colNum["B0"] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
      t = selectAndUpdate(collection, ind, val) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    if (ind == "B1" or ind == "B2" or ind == "B3"):
      payload = json.dumps({
        "selector": {
            "B": {
              "$elemMatch": {
                  ind : int(val) 
              }
            }
        }    })
      t = selectAndUpdateEmbedded(collection, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
    else:
      payload = json.dumps({
        "selector": {
            "B_ind": {
              "$elemMatch": {
                  ind : int(val) 
              }
            }
        }    })
      t = selectAndUpdateEmbedded(collection, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)

  collection = "embedding_a_in_b"
  # key 
  t = selectAndUpdate(collection, "BK", val)
  worksheet.write( get_colNum["B0"] + 1, get_rowNum[collection] + 1,t)
  payload = json.dumps({
   "selector": {
      "A_ind": {
         "$elemMatch": {
            "AK" : 67
         }
      }
   }
    })
  # foreign key 
  t = selectAndUpdateEmbedded(collection, payload)
  worksheet.write( get_colNum["A0"] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
      if (ind == "A1" or ind == "A2" or ind == "A3"):
        payload = json.dumps({
    "selector": {
        "A": {
          "$elemMatch": {
              ind : int(val)
          }
        }
    }
      })
        t = selectAndUpdateEmbedded(collection, payload) 
        worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
      else:
        payload = json.dumps({
    "selector": {
      "A_ind": {
         "$elemMatch": {
            ind : int(val)
         }
      }
   }
    })
        t = selectAndUpdateEmbedded(collection, payload) 
        worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    t = selectAndUpdate(collection, ind, val) 
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)

  workbook.close() 
