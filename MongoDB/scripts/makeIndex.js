use('tirocinio')


db.getCollection('A').createIndex({'AK': 1});
db.getCollection('B').createIndex({'BK': 1});

db.getCollection('A').createIndex({'A3': 1});               
db.getCollection('A').createIndex({'A4': 1});               
db.getCollection('A').createIndex({'A5': 1});               

db.getCollection('B').createIndex({'B3': 1});               
db.getCollection('B').createIndex({'B4': 1});               
db.getCollection('B').createIndex({'B5': 1});

db.getCollection('embedding_A_in_B').createIndex({'B4': 1});
db.getCollection('embedding_A_in_B').createIndex({'B5': 1});
db.getCollection('embedding_A_in_B').createIndex({'B6': 1});
db.getCollection('embedding_B_in_A').createIndex({'A4': 1});
db.getCollection('embedding_B_in_A').createIndex({'A5': 1});
db.getCollection('embedding_B_in_A').createIndex({'A6': 1});
db.getCollection('referencing_A_in_B').createIndex({'B4': 1});
db.getCollection('referencing_A_in_B').createIndex({'B5': 1});
db.getCollection('referencing_A_in_B').createIndex({'B6': 1});
db.getCollection('referencing_B_in_A').createIndex({'A4': 1});
db.getCollection('referencing_B_in_A').createIndex({'A5': 1});
db.getCollection('referencing_B_in_A').createIndex({'A6': 1});
