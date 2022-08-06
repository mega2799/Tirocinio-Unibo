Plan hash value: 42762562
 
------------------------------------------------------------------------------------
| Id  | Operation                   | Name | Rows  | Bytes | Cost (%CPU)| Time     |
------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT            |      |     1 |  1029 |     2   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID| A    |     1 |  1029 |     2   (0)| 00:00:01 |
|*  2 |   INDEX UNIQUE SCAN         | PK   |     1 |       |     1   (0)| 00:00:01 |
------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("AK"=7797
Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |    10 | 10290 |  4128   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    |    10 | 10290 |  4128   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A1"=3203
Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |   100 |   100K|  4128   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    |   100 |   100K|  4128   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A2"=307
Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      | 10000 |     9M|  4128   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    | 10000 |     9M|  4128   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A3"=9
Plan hash value: 3158792745
 
---------------------------------------------------------------------------------------------------
| Id  | Operation                           | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |             |    10 | 10290 |     5   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| A           |    10 | 10290 |     5   (0)| 00:00:01 |
|   2 |   BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  3 |    BITMAP INDEX SINGLE VALUE        | A_A4_BITMAP |       |       |            |          |
---------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - access("A4"=5231
Plan hash value: 3531648549
 
---------------------------------------------------------------------------------------------------
| Id  | Operation                           | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |             |   100 |   100K|    42   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| A           |   100 |   100K|    42   (0)| 00:00:01 |
|   2 |   BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  3 |    BITMAP INDEX SINGLE VALUE        | A_A5_BITMAP |       |       |            |          |
---------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - access("A5"=978
Plan hash value: 404362087
 
---------------------------------------------------------------------------------------------------
| Id  | Operation                           | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |             | 10000 |     9M|  3634   (1)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| A           | 10000 |     9M|  3634   (1)| 00:00:01 |
|   2 |   BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  3 |    BITMAP INDEX SINGLE VALUE        | A_A6_BITMAP |       |       |            |          |
---------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - access("A6"=6
Plan hash value: 923008758
 
----------------------------------------------------------------------------------------------------
| Id  | Operation                            | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
----------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                     |             |    10 | 20650 |     9   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                        |             |    10 | 20650 |     9   (0)| 00:00:01 |
|   2 |   TABLE ACCESS BY INDEX ROWID        | A           |     1 |  1029 |     2   (0)| 00:00:01 |
|*  3 |    INDEX UNIQUE SCAN                 | PK          |     1 |       |     1   (0)| 00:00:01 |
|   4 |   TABLE ACCESS BY INDEX ROWID BATCHED| B           |    10 | 10360 |     9   (0)| 00:00:01 |
|   5 |    BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  6 |     BITMAP INDEX SINGLE VALUE        | B_FK_BITMAP |       |       |            |          |
----------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - access("A"."AK"=7167
   6 - access("FAK"=7167
Plan hash value: 1717323899
 
---------------------------------------------------------------------------------------------
| Id  | Operation                     | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT              |             |    99 |   199K|  8309   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                 |             |    99 |   199K|  8309   (1)| 00:00:01 |
|   2 |   NESTED LOOPS                |             |    99 |   199K|  8309   (1)| 00:00:01 |
|*  3 |    TABLE ACCESS FULL          | A           |    10 | 10290 |  4128   (1)| 00:00:01 |
|   4 |    BITMAP CONVERSION TO ROWIDS|             |       |       |            |          |
|*  5 |     BITMAP INDEX SINGLE VALUE | B_FK_BITMAP |       |       |            |          |
|   6 |   TABLE ACCESS BY INDEX ROWID | B           |    10 | 10360 |  8309   (1)| 00:00:01 |
---------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A1"=3381
   5 - access("AK"="FAK"
Plan hash value: 1717323899
 
---------------------------------------------------------------------------------------------
| Id  | Operation                     | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT              |             |   992 |  2000K|  8792   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                 |             |   992 |  2000K|  8792   (1)| 00:00:01 |
|   2 |   NESTED LOOPS                |             |   992 |  2000K|  8792   (1)| 00:00:01 |
|*  3 |    TABLE ACCESS FULL          | A           |   100 |   100K|  4128   (1)| 00:00:01 |
|   4 |    BITMAP CONVERSION TO ROWIDS|             |       |       |            |          |
|*  5 |     BITMAP INDEX SINGLE VALUE | B_FK_BITMAP |       |       |            |          |
|   6 |   TABLE ACCESS BY INDEX ROWID | B           |    10 | 10360 |  8792   (1)| 00:00:01 |
---------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A2"=322
   5 - access("AK"="FAK"
Plan hash value: 1717323899
 
---------------------------------------------------------------------------------------------
| Id  | Operation                     | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT              |             | 99178 |   195M| 61819   (1)| 00:00:03 |
|   1 |  NESTED LOOPS                 |             | 99178 |   195M| 61819   (1)| 00:00:03 |
|   2 |   NESTED LOOPS                |             | 99178 |   195M| 61819   (1)| 00:00:03 |
|*  3 |    TABLE ACCESS FULL          | A           | 10000 |     9M|  4128   (1)| 00:00:01 |
|   4 |    BITMAP CONVERSION TO ROWIDS|             |       |       |            |          |
|*  5 |     BITMAP INDEX SINGLE VALUE | B_FK_BITMAP |       |       |            |          |
|   6 |   TABLE ACCESS BY INDEX ROWID | B           |    10 | 10360 | 61819   (1)| 00:00:03 |
---------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A3"=9
   5 - access("AK"="FAK"
Plan hash value: 1890719352
 
-----------------------------------------------------------------------------------------------------
| Id  | Operation                             | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
-----------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |             |    99 |   199K|    64   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                         |             |    99 |   199K|    64   (0)| 00:00:01 |
|   2 |   NESTED LOOPS                        |             |    99 |   199K|    64   (0)| 00:00:01 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| A           |    10 | 10290 |     5   (0)| 00:00:01 |
|   4 |     BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  5 |      BITMAP INDEX SINGLE VALUE        | A_A4_BITMAP |       |       |            |          |
|   6 |    BITMAP CONVERSION TO ROWIDS        |             |       |       |            |          |
|*  7 |     BITMAP INDEX SINGLE VALUE         | B_FK_BITMAP |       |       |            |          |
|   8 |   TABLE ACCESS BY INDEX ROWID         | B           |    10 | 10360 |    64   (0)| 00:00:01 |
-----------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   5 - access("A"."A4"=3299
   7 - access("AK"="FAK"
Plan hash value: 1710236477
 
-----------------------------------------------------------------------------------------------------
| Id  | Operation                             | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
-----------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |             |   992 |  2000K|   620   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                         |             |   992 |  2000K|   620   (1)| 00:00:01 |
|   2 |   NESTED LOOPS                        |             |   992 |  2000K|   620   (1)| 00:00:01 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| A           |   100 |   100K|    42   (0)| 00:00:01 |
|   4 |     BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  5 |      BITMAP INDEX SINGLE VALUE        | A_A5_BITMAP |       |       |            |          |
|   6 |    BITMAP CONVERSION TO ROWIDS        |             |       |       |            |          |
|*  7 |     BITMAP INDEX SINGLE VALUE         | B_FK_BITMAP |       |       |            |          |
|   8 |   TABLE ACCESS BY INDEX ROWID         | B           |    10 | 10360 |   620   (1)| 00:00:01 |
-----------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   5 - access("A"."A5"=712
   7 - access("AK"="FAK"
Plan hash value: 1238037621
 
-----------------------------------------------------------------------------------------------------
| Id  | Operation                             | Name        | Rows  | Bytes | Cost (%CPU)| Time     |
-----------------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |             | 99183 |   195M| 60831   (1)| 00:00:03 |
|   1 |  NESTED LOOPS                         |             | 99183 |   195M| 60831   (1)| 00:00:03 |
|   2 |   NESTED LOOPS                        |             | 99183 |   195M| 60831   (1)| 00:00:03 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| A           | 10000 |     9M|  3634   (1)| 00:00:01 |
|   4 |     BITMAP CONVERSION TO ROWIDS       |             |       |       |            |          |
|*  5 |      BITMAP INDEX SINGLE VALUE        | A_A6_BITMAP |       |       |            |          |
|   6 |    BITMAP CONVERSION TO ROWIDS        |             |       |       |            |          |
|*  7 |     BITMAP INDEX SINGLE VALUE         | B_FK_BITMAP |       |       |            |          |
|   8 |   TABLE ACCESS BY INDEX ROWID         | B           |    10 | 10360 | 60831   (1)| 00:00:03 |
-----------------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   5 - access("A"."A6"=3
   7 - access("AK"="FAK"
