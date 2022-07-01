use('tirocinio')

db.getCollection('embedding_A_in_B').createIndex({'B4': -1, 'B4': 'hashed' });
db.getCollection('embedding_A_in_B').createIndex({'B5': -1, 'B5': 'hashed' });
db.getCollection('embedding_A_in_B').createIndex({'B6': -1, 'B6': 'hashed' });
db.getCollection('embedding_B_in_A').createIndex({'A4': -1, 'A4': 'hashed' });
db.getCollection('embedding_B_in_A').createIndex({'A5': -1, 'A5': 'hashed' });
db.getCollection('embedding_B_in_A').createIndex({'A6': -1, 'A6': 'hashed' });
db.getCollection('referencing_A_in_B').createIndex({'B4': -1, 'B4': 'hashed' });
db.getCollection('referencing_A_in_B').createIndex({'B5': -1, 'B5': 'hashed' });
db.getCollection('referencing_A_in_B').createIndex({'B6': -1, 'B6': 'hashed' });
db.getCollection('referencing_B_in_A').createIndex({'A4': -1, 'A4': 'hashed' });
db.getCollection('referencing_B_in_A').createIndex({'A5': -1, 'A5': 'hashed' });
db.getCollection('referencing_B_in_A').createIndex({'A6': -1, 'A6': 'hashed' });
