use('tirocinio')

print("CUT")

printjson(db.getCollection('embedding_B_in_A').explain('executionStats').aggregate([ { $match: { "AK" : 99 } }]))
