# Report query MongoDB

## collection : "referencing_B_in_A"

```py
        # select A.*
        # from A
        # where Ax='val'
        
db.getCollection('referencing_B_in_A').aggregate(
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )

        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        
db.getCollection('referencing_B_in_A').aggregate([{'$match' : { ind : val} }, {'$unwind' : {  'path': "$B"}}, {
        '$lookup': {
        'from': 'B',
        'localField': 'B',
        'foreignField': 'BK',
        'as': 'B'
        }},{'$unwind' : {'path' : "$B"}}, {'$project' : {"B._id" : 0}}])

        # select B.*
        # from B
        # where Bx='val'
        db.getCollection('B').aggregate(
            [
                {
                    '$match' : { ind : val}
                }
            ]
        )

        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        db.getCollection('B').aggregate([{
        '$match': {
            ind : val
        }},{
        '$lookup': {
        'from' : 'referencing_B_in_A',
        'localField' : 'FAK',
        'foreignField' : 'AK',
        'as' : 'A'
        }}, {
        '$project': {
          "_id" : 0,
          "FAK" : 0,
          "A.B" : 0
        }},{'$unwind' : {'path' : "$A"}}])
```

## collection : "referencing_A_in_B"

```py

        # select A.*
        # from A
        # where Ax='val'
        db.getCollection('A').aggregate(
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )
        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        db.getCollection('referencing_B_in_A').aggregate([{'$match' : { ind  : val } }, {'$unwind': {  'path': "$B"}},{'$lookup': {'from': 'referencing_A_in_B','localField': 'B','foreignField': '_id','as': 'B'}}])
        # select B.*
        # from B
        # where Bx='val'
        db.getCollection('referencing_A_in_B').aggregate(
            [
                {
                    '$match' : { ind : val}
                }
            ]
        )

        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        db.getCollection('referencing_A_in_B').aggregate([{'$match' : {ind : val}},{
            '$lookup': {
            'from': 'A',
            'localField': 'AK',
            'foreignField': 'AK',
            'as': 'A'
            }},{
            '$project': {
            "A._id" : 0
            }},{'$unwind' : {'path': "$A"}}])
```

## collection : "embedding_B_in_A"

```py
        # select A.*
        # from A
        # where Ax='val'
        db.getCollection('embedding_B_in_A').aggregate(
                [
                    {
                        '$match' : { ind : val}
                    },{ '$project' : { "B" : 0}}
                ]
            )

        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        query =(
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )

        # select B.*
        # from B
        # where Bx='val'
        db.getCollection('embedding_B_in_A').aggregate([{'$match': {"B." + ind : val}},{'$unwind': {'path' : "$B"}},{'$match' : {"B." + ind : val}}, {'$project':{"B" : 1, "_id" : 0}}])

        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        db.getCollection('embedding_B_in_A').aggregate([{'$match': {"B." + ind : val}},{'$unwind': {'path' : "$B"}},{'$match' : {"B." + ind : val}}])
```

## collection : "embedding_A_in_B"

```py
        # select A.*
        # from A
        # where Ax='val'
        db.getCollection('embedding_A_in_B').aggregate([{'$match': {"A." + ind : val}},{'$project': {"A" : 1, "_id" : 0}},{'$unwind' : {'path' : "$A"}}])

        # select A.*, B.*
        # from A join B on (A.AK=B.AK)
        # where Ax='val'
        db.getCollection('embedding_A_in_B').aggregate([{'$match': {"A." + ind : val}}])

        # select B.*
        # from B
        # where Bx='val'
        query =(
                [
                    {
                        '$match' : { ind : val}
                    },{ '$project' : { "A" : 0}}
                ]
            )

        # select A.*, B.*
        # from A join B on (A.AK=B.BK)
        # where Bx='val
        db.getCollection('embedding_A_in_B').aggregate(
                [
                    {
                        '$match' : { ind : val}
                    }
                ]
            )
```
