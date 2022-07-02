import requests
import json
import os

ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]
ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]



collections = os.listdir('../../dataJSON')
collection_titles = [ l.lower() for l in collections] # lower case altrimenti couchdb si arrabbia...

print("On which collection should i run the query")
n = int(input("0)embedding_A_in_B.json\n1)embedding_B_in_A.json\n2)referencing_A_in_B.json\n3)referencing_B_in_A.json\n\n"))

collection = collection_titles[n][:-5]

print(collection)
if n%2 == 1:
    print("On which index should i run the query")
    i = input("0)A1 \n1)A2 \n2)A3 \n3)A4 \n4)A5 \n5)A6\n\n")
    ind = ind_a[int(i)]
else:
    print("On which index should i run the query")
    i = input("0)B1 \n1)B2 \n2)B3 \n3)B4 \n4)B5 \n5)B6\n\n")
    ind = ind_b[int(i)]


val = input("On which value?\n\n")

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

print(payload)

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
