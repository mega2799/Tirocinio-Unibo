import requests
import json
import os 

collections_a = [ 'referencing_b_in_a', 'embedding_b_in_a']
collections_b = ['embedding_a_in_b',  'referencing_a_in_b']

ind_a= ["A4",  "A5", "A6"]
ind_b= ["B4",  "B5", "B6"]

# A 
url = "http://admin:admin@127.0.0.1:5984/a/_index?partitioned=true"
for ind  in ind_a:
  payload = json.dumps({
    "index": {
      "fields": [
        ind
      ]
    },
    "name": ind + "-index",
    "type": "json"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)
payload = json.dumps({
  "index": {
    "fields": [
      "AK"
    ]
  },
  "name": "AK" + "-index",
  "type": "json"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

# B 
url = "http://admin:admin@127.0.0.1:5984/b/_index?partitioned=true"
for ind  in ind_b:
  payload = json.dumps({
    "index": {
      "fields": [
        ind
      ]
    },
    "name": ind + "-index",
    "type": "json"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)

payload = json.dumps({
  "index": {
    "fields": [
      "BK"
    ]
  },
  "name": "BK" + "-index",
  "type": "json"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

for collection in collections_a:
    url = "http://admin:admin@127.0.0.1:5984/" + collection + "/_index?partitioned=true"
    for ind  in ind_a:
        payload = json.dumps({
          "index": {
            "fields": [
              ind
            ]
          },
          "name": ind + "-index",
          "type": "json"
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

for collection in collections_b:
    url = "http://admin:admin@127.0.0.1:5984/" + collection + "/_index?partitioned=true"
    for ind  in ind_b:
        payload = json.dumps({
          "index": {
            "fields": [
              ind
            ]
          },
          "name": ind + "-index",
          "type": "json"
        })
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

url = "http://admin:admin@127.0.0.1:5984/referencing_a_in_b/_index?partitioned=true"
payload = json.dumps({
  "index": {
    "fields": [
      "AK"
    ]
  },
  "name": "AK" + "-index",
  "type": "json"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# emb AB
url = "http://admin:admin@127.0.0.1:5984/embedding_a_in_b/_index?partitioned=true"
for ind in ind_a:
  payload = json.dumps({
    "index": {
      "fields": [
        "A." + ind
      ]
    },
    "name": "A." + ind + "-index",
    "type": "json"
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)

# emb BA
url = "http://admin:admin@127.0.0.1:5984/embedding_b_in_a/_index?partitioned=true"
for ind in ind_b:
  payload = json.dumps({
    "index": {
      "fields": [
        "B." + ind
      ]
    },
    "name": "B." + ind + "-index",
    "type": "json"
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)

# ref BA
url = "http://admin:admin@127.0.0.1:5984/referencing_b_in_a/_index?partitioned=true"
payload = json.dumps({
  "index": {
    "fields": [
      "B"
    ]
  },
  "name": "B" + "-index",
  "type": "json"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
