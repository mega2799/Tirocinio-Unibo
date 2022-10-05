from random import randint
import pymongo
import json
import time
import xlsxwriter

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

get_rowNum = {'embedding_A_in_B' : 0,'embedding_B_in_A' : 1,'referencing_B_in_A' : 2,'referencing_A_in_B' : 3}
get_colNum = {'A0' : 0,
'A1' : 1,
'A2' : 2,
'A3' : 3,
'A4' : 4,
'A5' : 5,
'A6' : 6,
'B0' : 7,
'B1' : 8,
'B2' : 9,
'B3' : 10,
'B4' : 11,
'B5' : 12,
'B6' : 13}
""" 'A0join' : 14,
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
'B6join' : 27 """


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

""" def update_cost_once(collection, ind, value, mod_ind):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    return mydb.command(
        'explain', 
        {
            'update': collection,
            'updates' : [
              {'q' : {ind : value},
              'u' : {'$set' : {mod_ind : "AAAAAA"
              }}}]
        }, 
        verbosity='executionStats'
    )
 """

def update_cost_once(collection, ind, value, mod_ind):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    res = mydb.command(
        'explain', 
        {
            'update': collection,
            'updates' : [
              {'q' : {ind : value},
              'u' : {'$set' : {mod_ind : "AAAA"
              }}}]
        }, 
        verbosity='executionStats'
    )
    for key, value in res.items():
        print("----" ,key, "--->", value)
    if "stages" in list(res.keys()):
        time = (res["stages"][0]["$cursor"]["executionStats"]["executionTimeMillis"])
    else:
        time = (res["executionStats"]["executionTimeMillis"])
    if res["executionStats"] == False:
        print(collection, ind)
        exit(0)
    return time


def exec_cost(collection, query):
    myclient = pymongo.MongoClient("mongodb://root:pass12345@localhost:27017/")
    mydb = myclient["tirocinio"]
    print("plan", query)
    t = []
    for i in range(10):
      res = mydb.command(
          'explain', 
          {
              'aggregate': collection, 
              'pipeline': query, 
              'cursor': {}
          }, 
          verbosity='executionStats'
      ) 
      if "stages" in list(res.keys()):
          time = (res["stages"][0]["$cursor"]["executionStats"]["executionTimeMillis"])
          docum = (res["stages"][0]["$cursor"]["executionStats"]["nReturned"])
      else:
          time = (res["executionStats"]["executionTimeMillis"])
          docum = (res["executionStats"]["nReturned"])
      if docum == 0:
          print(collection, ind, docum)
          exit(0)
      t.append(time)
    return sum(t)/10
      
workbook = xlsxwriter.Workbook('MongoDBStatCRUD.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.set_column(1, 1, 20)
worksheet.set_column(2, 2, 20)
worksheet.set_column(3, 3, 20)
worksheet.set_column(4, 4, 20)

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
""" worksheet.write_string('A16' , 'A0j', bold)
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
worksheet.write_string('A29' , 'B6j', bold) """
worksheet.write_string('B1', 'embedding_A_in_B', bold)
worksheet.write_string('C1', 'embedding_B_in_A', bold)
worksheet.write_string('D1', 'referencing_A_in_B', bold)
worksheet.write_string('E1', 'referencing_B_in_A', bold)

if __name__ == "__main__":
    collection = "referencing_B_in_A"
    #update_cost_once(collection, "AK", 80176, "A7")
    #key 
    res = update_cost_once(collection, "AK", 5192 , "A7")
    worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1 , res)
    # foreign key 
    res = update_cost_once(collection, "BK", 5192 , "A7")
    worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        res = update_cost_once(collection, ind, get_random_indexed_int_A(ind) , "A7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        res = update_cost_once("B", ind, get_random_indexed_int_B(ind) , "B7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)

    collection = "referencing_A_in_B"
    #key 
    res = update_cost_once(collection, "BK", 5192 , "B7")
    worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1 , res)
    #foreign key 
    res = update_cost_once(collection, "AK", 5192 , "B7")
    worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        res = update_cost_once("A", ind, get_random_indexed_int_A(ind) , "A7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        res = update_cost_once(collection, ind, get_random_indexed_int_B(ind) , "B7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)
    
    collection = "embedding_B_in_A"
    #key 
    res = update_cost_once(collection, "AK", 5192 , "A7")
    worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1 , res)
    #foreign key 
    res = update_cost_once(collection, "B.BK", 5192 , "A7")
    worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1 , res)
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
        res = update_cost_once(collection, ind, get_random_indexed_int_A(ind) , "A7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        res = update_cost_once(collection, "B." + ind, get_random_indexed_int_B(ind) , "A7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)

    collection = "embedding_A_in_B"
    #key 

    res = update_cost_once(collection, "BK", 5192 , "B7")
    worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1 , res)
    #foreign key 
    res = update_cost_once(collection, "A.AK", 5192 , "B7")
    worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_a:
        # select A.*
        # from A
        # where Ax='val'
        res = update_cost_once(collection, "A." + ind, get_random_indexed_int_A(ind) , "B7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)
    for ind in ind_b:
        # select B.*
        # from B
        # where Bx='val'
        res = update_cost_once(collection, ind, get_random_indexed_int_B(ind) , "B7")
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , res)
    workbook.close() 