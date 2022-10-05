import requests
import json
import os

collections = os.listdir('../../dataJSON')
collection_titles = [ l.lower() for l in collections] # lower case altrimenti couchdb si arrabbia...


# make DB
#for collection in collection_titles:
#    url = "http://admin:admin@127.0.0.1:5984/" + collection[:-5]
#
#    payload={}
#    headers = {
#      'Accept': 'application/json',
#      'Content-Type': 'application/json'
#    }
#
#    response = requests.request("PUT", url, headers=headers, data=payload)
#
#    print(response.text)

# send Json 


payload = json.loads("../../dataJson/" + collections[0])


headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

print(payload)
# response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)