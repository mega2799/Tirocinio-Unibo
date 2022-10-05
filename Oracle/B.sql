Plan hash value: 3484949970
 
------------------------------------------------------------------------------------
| Id  | Operation                   | Name | Rows  | Bytes | Cost (%CPU)| Time     |
------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT            |      |     1 |  1130 |     2   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID| B    |     1 |  1130 |     2   (0)| 00:00:01 |
|*  2 |   INDEX UNIQUE SCAN         | PKB  |     1 |       |     1   (0)| 00:00:01 |
------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("BK"=5589
Plan hash value: 1911541843
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |  8278 |  9134K| 45380   (1)| 00:00:02 |
|*  1 |  TABLE ACCESS FULL| B    |  8278 |  9134K| 45380   (1)| 00:00:02 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("B1"=4039
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 1911541843
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |  8278 |  9134K| 45381   (1)| 00:00:02 |
|*  1 |  TABLE ACCESS FULL| B    |  8278 |  9134K| 45381   (1)| 00:00:02 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("B2"=841
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 1911541843
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      | 90213 |    97M| 45383   (1)| 00:00:02 |
|*  1 |  TABLE ACCESS FULL| B    | 90213 |    97M| 45383   (1)| 00:00:02 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("B3"=5
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 3753266301
 
--------------------------------------------------------------------------------------------
| Id  | Operation                           | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |      |    10 | 11300 |    16   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| B    |    10 | 11300 |    16   (0)| 00:00:01 |
|*  2 |   INDEX RANGE SCAN                  | B_B4 |    10 |       |     3   (0)| 00:00:01 |
--------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("B4"=1008
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 2666462047
 
--------------------------------------------------------------------------------------------
| Id  | Operation                           | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |      |  1000 |  1103K|  1214   (1)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| B    |  1000 |  1103K|  1214   (1)| 00:00:01 |
|*  2 |   INDEX RANGE SCAN                  | B_B5 |  1000 |       |     5   (0)| 00:00:01 |
--------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("B5"=473
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 1911541843
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      | 71640 |    77M| 45386   (1)| 00:00:02 |
|*  1 |  TABLE ACCESS FULL| B    | 71640 |    77M| 45386   (1)| 00:00:02 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("B6"=2
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 2094168580
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |     1 |  2247 |     3   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |     1 |  2247 |     3   (0)| 00:00:01 |
|   2 |   TABLE ACCESS BY INDEX ROWID| B    |     1 |  1130 |     2   (0)| 00:00:01 |
|*  3 |    INDEX UNIQUE SCAN         | PKB  |     1 |       |     1   (0)| 00:00:01 |
|   4 |   TABLE ACCESS BY INDEX ROWID| A    |     1 |  1117 |     1   (0)| 00:00:01 |
|*  5 |    INDEX UNIQUE SCAN         | PK   |     1 |       |     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - access("B"."BK"=8336
   5 - access("AK"="FAK"
Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |  8278 |    17M|  3990   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |  8278 |    17M|  3990   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |  1129M|    17M|  3990   (1)| 00:00:01 |
|   3 |    TABLE ACCESS FULL         | A    | 91380 |    97M|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|*  5 |   TABLE ACCESS BY INDEX ROWID| B    |     1 |  1130 |     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("AK"="FAK"
   5 - filter("B"."B1"=6448
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |  8278 |    17M|  3990   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |  8278 |    17M|  3990   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |  1129M|    17M|  3990   (1)| 00:00:01 |
|   3 |    TABLE ACCESS FULL         | A    | 91380 |    97M|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|*  5 |   TABLE ACCESS BY INDEX ROWID| B    |     1 |  1130 |     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("AK"="FAK"
   5 - filter("B"."B2"=123
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      | 84907 |   181M|  3990   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      | 84907 |   181M|  3990   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |  1129M|   181M|  3990   (1)| 00:00:01 |
|   3 |    TABLE ACCESS FULL         | A    | 91380 |    97M|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|*  5 |   TABLE ACCESS BY INDEX ROWID| B    |     1 |  1130 |     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("AK"="FAK"
   5 - filter("B"."B3"=9
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
Plan hash value: 3451358140
 
----------------------------------------------------------------------------------------------
| Id  | Operation                             | Name | Rows  | Bytes | Cost (%CPU)| Time     |
----------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |      |    10 | 22470 |    26   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                         |      |    10 | 22470 |    26   (0)| 00:00:01 |
|   2 |   NESTED LOOPS                        |      |    10 | 22470 |    26   (0)| 00:00:01 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| B    |    10 | 11300 |    16   (0)| 00:00:01 |
|*  4 |     INDEX RANGE SCAN                  | B_B4 |    10 |       |     3   (0)| 00:00:01 |
|*  5 |    INDEX UNIQUE SCAN                  | PK   |     1 |       |     0   (0)| 00:00:01 |
|   6 |   TABLE ACCESS BY INDEX ROWID         | A    |     1 |  1117 |     1   (0)| 00:00:01 |
----------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("B"."B4"=4410
   5 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
Plan hash value: 2955774714
 
----------------------------------------------------------------------------------------------
| Id  | Operation                             | Name | Rows  | Bytes | Cost (%CPU)| Time     |
----------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |      |  1000 |  2194K|  2214   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                         |      |  1000 |  2194K|  2214   (1)| 00:00:01 |
|   2 |   NESTED LOOPS                        |      |  1000 |  2194K|  2214   (1)| 00:00:01 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| B    |  1000 |  1103K|  1214   (1)| 00:00:01 |
|*  4 |     INDEX RANGE SCAN                  | B_B5 |  1000 |       |     5   (0)| 00:00:01 |
|*  5 |    INDEX UNIQUE SCAN                  | PK   |     1 |       |     0   (0)| 00:00:01 |
|   6 |   TABLE ACCESS BY INDEX ROWID         | A    |     1 |  1117 |     1   (0)| 00:00:01 |
----------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("B"."B5"=191
   5 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      | 84907 |   181M|  3990   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      | 84907 |   181M|  3990   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |  1129M|   181M|  3990   (1)| 00:00:01 |
|   3 |    TABLE ACCESS FULL         | A    | 91380 |    97M|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|*  5 |   TABLE ACCESS BY INDEX ROWID| B    |     1 |  1130 |     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("AK"="FAK"
   5 - filter("B"."B6"=3
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
