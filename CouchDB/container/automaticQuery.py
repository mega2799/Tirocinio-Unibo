from random import randint
from ntpath import join
import requests
import json
import xlsxwriter
import numpy as np
import os


expA = 3

expB = 4

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
worksheet.write_string('A16' , 'A0j', bold)
worksheet.write_string('A17' , 'A1j', bold)
worksheet.write_string('A18' , 'A2j', bold)
worksheet.write_string('A19' , 'A3j', bold)
worksheet.write_string('A20' , 'A4j', bold)
worksheet.write_string('A21' , 'A5j', bold)
worksheet.write_string('A22' , 'A6j', bold)
worksheet.write_string('A23' , 'B0j', bold)
worksheet.write_string('A24' , 'B1j', bold)
worksheet.write_string('A25' , 'B2j', bold)
worksheet.write_string('A26' , 'B3j', bold)
worksheet.write_string('A27' , 'B4j', bold)
worksheet.write_string('A28' , 'B5j', bold)
worksheet.write_string('A29' , 'B6j', bold)


get_rowNum = {'embedding_a_in_b' : 0,'embedding_b_in_a' : 1,'referencing_b_in_a' : 2,'referencing_a_in_b' : 3}
get_colNum = {'A0' : 0,'A1' : 1,'A2' : 2,'A3' : 3,'A4' : 4,'A5' : 5,'A6' : 6,
'B0' : 7,'B1' : 8,'B2' : 9,'B3' : 10,'B4' : 11,'B5' : 12,
    'B6' : 13,
'A0join' : 14,
'A1join' : 15,
'A2join' : 16,
'A3join' : 17,
'A4join' : 18,
'A5join' : 19,
'A6join' : 20,
'B0join' : 21,
'B1join' : 22,
'B2join' : 23,
'B3join' : 24,
'B4join' : 25,
'B5join' : 26,
'B6join' : 27}


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

def queryRun(collection, ind, payload):
  url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
  time = 0
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  resp = json.loads(response.text)
  check(resp, collection, ind)
  time += resp["execution_stats"]['execution_time_ms']
  # worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
  print("sel time: " )
  print(str(time) + " ms") 
  return time

def check(p, col, ind):
  if p["execution_stats"]['results_returned'] == 0:
    print(col)
    print(ind)
    print(p)
    print("ERRROR")
    exit(1)

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
  check(resp, collection, ind)
  time += resp["execution_stats"]['execution_time_ms']
  # worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
  print("sel time: " )
  print(str(time) + " ms") 
  return time


def simpleSelectionResp(collection, ind, value):
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
  check(resp, collection, ind)
  time += resp["execution_stats"]['execution_time_ms']
  # worksheet.write(get_rowNum[collection] + 1, get_colNum[ind] + 1, time)
  print("sel time: " )
  print(str(time) + " ms") 
  return time, resp



def refBA():
  collection = "referencing_b_in_a"
  print("i'm in " + collection)
  # key 
  t = simpleSelection(collection, "AK", val)
  worksheet.write( get_colNum["A0"] + 1, get_rowNum[collection] + 1,t)
  # foreign key 
  t = simpleSelection("b", "BK", 67)
  worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1,t)
  # key join 
  url = "http://admin:admin@127.0.0.1:5984/" + "referencing_b_in_a" +"/_find"
  payload = json.dumps({
  "selector": {
      "_id" : val
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
  # print(resp["docs"])
  foreign_keys = [list(x.values())[10] for x in resp["docs"]]
  url = "http://admin:admin@127.0.0.1:5984/" + "b" +"/_find"
  for lis in foreign_keys:
      for key in lis:
        payload = json.dumps({
          "selector": {
            "BK" : key
          },
          "execution_stats": True
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        resp = json.loads(response.text)
        time += resp["execution_stats"]['execution_time_ms']
  worksheet.write(get_colNum["A0join"] + 1,get_rowNum[collection] + 1, time)
  print('im in FK join ')
  # FK join 
  url = "http://admin:admin@127.0.0.1:5984/" + "b" +"/_find"
  payload = json.dumps({
  "selector": {
      "BK" : int(val)
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
  check(resp, collection, "BO")
  time += resp["execution_stats"]['execution_time_ms']
  time += simpleSelection(collection, "AK", val)
  worksheet.write(get_colNum["B0join"] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
    t = simpleSelection(collection, ind, val)
    worksheet.write( get_colNum[ind] + 1, get_rowNum[collection] + 1,t)
      # select A.*, B.*
      # from A join B on (A.AK=B.AK)
      # where Ax='val'
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
    check(resp, collection, ind)
    time += resp["execution_stats"]['execution_time_ms']
    # print(resp["docs"])
    foreign_keys = [list(x.values())[10] for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/" + "b" +"/_find"
    for lis in foreign_keys:
        for key in lis:
          payload = json.dumps({
            "selector": {
              "BK" : key
            },
            "execution_stats": True
          })
          response = requests.request("POST", url, headers=headers, data=payload)
          resp = json.loads(response.text)
          check(resp, collection, ind)
          time += resp["execution_stats"]['execution_time_ms']
    worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, time)
    print("join time: " )
    print(str(time) + " ms") 
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx= vaal
    t = simpleSelection("b", ind, val)
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
      # select A.*, B.*
      # from A join B on (A.AK=B.BK)
      # where Bx='val
    print("index on B")
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
    check(resp, collection, ind)
    time += resp["execution_stats"]['execution_time_ms']
    foreign_keys = [str(list(x.values())[2]) for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/referencing_a_in_b/_find"
    for key in foreign_keys:
      payload = json.dumps({
        "selector": {
          "_id" : str(key) 
        },
        "execution_stats": True
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      check(resp, collection, ind)
      resp = json.loads(response.text)
      time += resp["execution_stats"]['execution_time_ms']
    worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, time)
    print("join time: " )
    print(str(time) + " ms") 

def refAB():
  collection = "referencing_a_in_b"
  print("i'm in " + collection)
  # key 
  t = simpleSelection(collection, "BK", val)
  worksheet.write( get_colNum["B0"] + 1, get_rowNum[collection] + 1,t)
  # for key 
  t = simpleSelection("a", "AK", val)
  worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1,t)
  # join 
  t, resp = simpleSelectionResp(collection, "BK", val)
  fk = [str(list(x.values())[2]) for x in resp["docs"]]
  t += simpleSelection("a", "AK", val)
  worksheet.write( get_colNum["B0join"] + 1, get_rowNum[collection] + 1,t)
  # key join Aj0
  t,resp = simpleSelectionResp("a", "AK", int(fk[0]))
  fk = [str(list(x.values())[2]) for x in resp["docs"]]
  t += simpleSelection(collection, "AK", int(fk[0]))
  worksheet.write( get_colNum["A0join"] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
    t = simpleSelection("a", ind, val)
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
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
    check(resp, collection, ind)
    time += resp["execution_stats"]['execution_time_ms']
##################### TESTARE ##################################################
    foreign_keys = [list(x.values())[2] for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
    for key in foreign_keys:
      payload = json.dumps({
        "selector": {
          "_id" : str(key)
        },
        "execution_stats": True
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      resp = json.loads(response.text)
      check(resp, collection, ind)
      time += resp["execution_stats"]['execution_time_ms']
    worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, time)
    print("join time: " )
    print(str(time) + " ms") 
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    t = simpleSelection(collection, ind, val)
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
      # select A.*, B.*
      # from A join B on (A.AK=B.BK)
      # where Bx='val
  ##################### TESTARE ##################################################
  # join tra referencing_A_in_B (esterna) e A (interna)
    url = "http://admin:admin@127.0.0.1:5984/" + collection +"/_find"
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
    check(resp, collection, ind)
    time += resp["execution_stats"]['execution_time_ms']
  ### qui dovrei prendere le chiavi di AK e per ognuna selezionare il doc di A
    foreign_keys = [list(x.values())[3] for x in resp["docs"]]
    url = "http://admin:admin@127.0.0.1:5984/" + "a" +"/_find"
    for key in foreign_keys:
      payload = json.dumps({
        "selector": {
          "AK" : key
        },
        "execution_stats": True
      })
      response = requests.request("POST", url, headers=headers, data=payload)
      resp = json.loads(response.text)
      check(resp, collection, ind)
      time += resp["execution_stats"]['execution_time_ms']
    worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, time)
    print("join time: " )
    print(str(time) + " ms")


if __name__ == "__main__":

  val = "8"

  #refBA()
  #refAB()

  collection = "embedding_b_in_a"
  # foreign key 
  payload = json.dumps({
      "selector": {
          "B_ind": {
            "$elemMatch": {
                "BK" : int(val) 
            }
          }
      },
      "fields": [
          "B", "B_ind"
      ],
      "execution_stats": True
    })
  t = queryRun(collection, "BK", payload) 
  worksheet.write( get_colNum["B0"] + 1,get_rowNum[collection] + 1, t)
  # foreign key join
  payload = json.dumps({
      "selector": {
          "B_ind": {
            "$elemMatch": {
                "BK" : int(val) 
            }
          }
      },
      "execution_stats": True
    })
  t = queryRun(collection, "BK", payload) 
  worksheet.write( get_colNum["B0join"] + 1,get_rowNum[collection] + 1, t)
  payload = json.dumps({
      "selector": {
          "AK" : int(val) 
      },
      "fields": [
          "_id",
          "AK",
          "A1",
          "A2",
          "A3",
          "A4",
          "A5",
          "A6",
          "A7"
      ],
      "execution_stats": True
    })
  t = queryRun(collection, "A0", payload) 
  worksheet.write( get_colNum["A0"] + 1,get_rowNum[collection] + 1, t)
  # key join
  t = simpleSelection(collection, "AK", val)
  worksheet.write( get_colNum["A0join"] + 1, get_rowNum[collection] + 1,t)
  for ind in ind_a:
      # select A.*
      # from A
      # where Ax='val'
      payload = json.dumps({
      "selector": {
          ind : int(val) 
      },
      "fields": [
          "_id",
          "AK",
          "A1",
          "A2",
          "A3",
          "A4",
          "A5",
          "A6",
          "A7"
      ],
      "execution_stats": True
    })
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
      # select A.*, B.*
      # from A join B on (A.AK=B.AK)
      # where Ax='val'
      t = simpleSelection(collection, ind, val) ###################################### aggiungere indice con join
      worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, t)
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    if (ind == "B1" or ind == "B2" or ind == "B3"):
      print("query on B[] ind: ", ind)
      payload = json.dumps({
        "selector": {
            "B": {
              "$elemMatch": {
                  ind : int(val) 
              }
            }
        },
        "fields": [
            "B", "B_ind"
        ],
        "execution_stats": True
      })
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
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
      t = queryRun(collection, ind, payload)  
      worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, t)
    else:
      print("query on B_ind[] ind: ", ind)
      payload = json.dumps({
        "selector": {
            "B_ind": {
              "$elemMatch": {
                  ind : int(val) 
              }
            }
        },
        "fields": [
            "B", "B_ind"
        ],
        "execution_stats": True
      })
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
      payload = json.dumps({
        "selector": {
            "B_ind": {
              "$elemMatch": {
                  ind : int(val)
              }
            }
        },
        "execution_stats": True
      })
      t = queryRun(collection, ind, payload)  
      worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, t)


  collection = "embedding_a_in_b"
  # key 
  payload = json.dumps({
   "selector": {
      "_id": val 
      },
      "fields": [
          "_id",
          "BK",
          "B1",
          "B2",
          "B3",
          "B4",
          "B5",
          "B6",
          "B7"
      ],
      "execution_stats": True
    })
  t = queryRun(collection, "B0", payload) 
  worksheet.write(get_colNum["B0"] + 1,get_rowNum[collection] + 1, t)
  # key join 
  payload = json.dumps({
   "selector": {
      "_id": val 
      },
      "execution_stats": True
    })
  t = queryRun(collection, "B0j", payload) 
  worksheet.write( get_colNum["B0join"] + 1, get_rowNum[collection] + 1,t)
  # fk 
  payload = json.dumps({
   "selector": {
      "A_ind": {
         "$elemMatch": {
            "AK" : int(val)
         }
      }
   },
      "fields": [
          "A", "A_ind"
      ],
      "execution_stats": True
    })
  t = queryRun(collection, "A0", payload) 
  worksheet.write( get_colNum["A0"] + 1,get_rowNum[collection] + 1, t)
  # fk  join
  payload = json.dumps({
   "selector": {
      "A_ind": {
         "$elemMatch": {
            "AK" : int(val)
         }
      }
   },
      "execution_stats": True
    })
  t = queryRun(collection, "A0join", payload) 
  worksheet.write( get_colNum["A0join"] + 1,get_rowNum[collection] + 1, t)

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
   },
      "fields": [
          "A"
      ],
      "execution_stats": True
    })
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
      # select A.*, B.*
      # from A join B on (A.AK=B.AK)
      # where Ax='val'
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
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, t)
    else:
      payload = json.dumps({
   "selector": {
      "A_ind": {
         "$elemMatch": {
            ind : int(val)
         }
      }
   },
      "fields": [
          "A", "A_ind"
      ],
      "execution_stats": True
    })
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
      # select A.*, B.*
      # from A join B on (A.AK=B.AK)
      # where Ax='val'
      payload = json.dumps({
   "selector": {
      "A_ind": {
         "$elemMatch": {
            ind : int(val)
         }
      }
   },
      "execution_stats": True
    })
      t = queryRun(collection, ind, payload) 
      worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, t)
  for ind in ind_b:
      # select B.*
      # from B
      # where Bx='val'
    payload = json.dumps({
   "selector": {
      ind : int(val) 
      },
      "fields": [
          "_id",
          "BK",
          "B1",
          "B2",
          "B3",
          "B4",
          "B5",
          "B6",
          "B7"
      ],
      "execution_stats": True
    })
    t = queryRun(collection, ind, payload) 
    worksheet.write( get_colNum[ind] + 1,get_rowNum[collection] + 1, t)
    ########################################################################################## fin qua
      # select A.*, B.*
      # from A join B on (A.AK=B.BK)
      # where Bx='val
    t = simpleSelection(collection, ind, payload)  
    worksheet.write( get_colNum[(ind + "join")] + 1,get_rowNum[collection] + 1, t)

  workbook.close() 



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
