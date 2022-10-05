Plan hash value: 42762562
 
------------------------------------------------------------------------------------
| Id  | Operation                   | Name | Rows  | Bytes | Cost (%CPU)| Time     |
------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT            |      |     1 |  1117 |     2   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID| A    |     1 |  1117 |     2   (0)| 00:00:01 |
|*  2 |   INDEX UNIQUE SCAN         | PK   |     1 |       |     1   (0)| 00:00:01 |
------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("AK"=534

Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |   914 |   997K|  3988   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    |   914 |   997K|  3988   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A1"=329
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |   233 |   254K|  3989   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    |   233 |   254K|  3989   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A2"=273
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      | 10956 |    11M|  3989   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    | 10956 |    11M|  3989   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A3"=4
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 1487816151
 
--------------------------------------------------------------------------------------------
| Id  | Operation                           | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |      |    10 | 11170 |    12   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| A    |    10 | 11170 |    12   (0)| 00:00:01 |
|*  2 |   INDEX RANGE SCAN                  | A_A4 |    10 |       |     1   (0)| 00:00:01 |
--------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("A4"=5210
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 2273292
 
--------------------------------------------------------------------------------------------
| Id  | Operation                           | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                    |      |   100 |   109K|   111   (0)| 00:00:01 |
|   1 |  TABLE ACCESS BY INDEX ROWID BATCHED| A    |   100 |   109K|   111   (0)| 00:00:01 |
|*  2 |   INDEX RANGE SCAN                  | A_A5 |   100 |       |     1   (0)| 00:00:01 |
--------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   2 - access("A5"=491
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 2248738933
 
--------------------------------------------------------------------------
| Id  | Operation         | Name | Rows  | Bytes | Cost (%CPU)| Time     |
--------------------------------------------------------------------------
|   0 | SELECT STATEMENT  |      |  9324 |     9M|  3989   (1)| 00:00:01 |
|*  1 |  TABLE ACCESS FULL| A    |  9324 |     9M|  3989   (1)| 00:00:01 |
--------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   1 - filter("A6"=1
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 4162912218
 
---------------------------------------------------------------------------------------------
| Id  | Operation                            | Name | Rows  | Bytes | Cost (%CPU)| Time     |
---------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                     |      |    10 | 22470 |     2   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                        |      |    10 | 22470 |     2   (0)| 00:00:01 |
|   2 |   TABLE ACCESS BY INDEX ROWID        | A    |     1 |  1117 |     2   (0)| 00:00:01 |
|*  3 |    INDEX UNIQUE SCAN                 | PK   |     1 |       |     1   (0)| 00:00:01 |
|   4 |   TABLE ACCESS BY INDEX ROWID BATCHED| B    |    10 | 11300 |     0   (0)| 00:00:01 |
|*  5 |    INDEX RANGE SCAN                  | B_FK |    10 |       |     0   (0)| 00:00:01 |
---------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - access("A"."AK"=1111
   5 - access("FAK"=1111
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2
Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |    11M|  1773M|  3989   (1)| 00:00:01 |
|*  3 |    TABLE ACCESS FULL         | A    |   914 |   997K|  3988   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|   5 |   TABLE ACCESS BY INDEX ROWID| B    |   906 |   999K|     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A1"=3124
   4 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |    11M|  1773M|  3989   (1)| 00:00:01 |
|*  3 |    TABLE ACCESS FULL         | A    |   914 |   997K|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|   5 |   TABLE ACCESS BY INDEX ROWID| B    |   906 |   999K|     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A2"=142
   4 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |    89M|  1773M|  3989   (1)| 00:00:01 |
|*  3 |    TABLE ACCESS FULL         | A    |  7226 |  7882K|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|   5 |   TABLE ACCESS BY INDEX ROWID| B    |   115 |   126K|     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A3"=2
   4 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 1504201086
 
----------------------------------------------------------------------------------------------
| Id  | Operation                             | Name | Rows  | Bytes | Cost (%CPU)| Time     |
----------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |      |   123K|   264M|    12   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                         |      |   123K|   264M|    12   (0)| 00:00:01 |
|   2 |   NESTED LOOPS                        |      |   123K|   264M|    12   (0)| 00:00:01 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| A    |    10 | 11170 |    12   (0)| 00:00:01 |
|*  4 |     INDEX RANGE SCAN                  | A_A4 |    10 |       |     1   (0)| 00:00:01 |
|*  5 |    INDEX RANGE SCAN                   | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|   6 |   TABLE ACCESS BY INDEX ROWID         | B    | 12356 |    13M|     0   (0)| 00:00:01 |
----------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("A"."A4"=1684
   5 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 1360178174
 
----------------------------------------------------------------------------------------------
| Id  | Operation                             | Name | Rows  | Bytes | Cost (%CPU)| Time     |
----------------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT                      |      |   827K|  1773M|   111   (0)| 00:00:01 |
|   1 |  NESTED LOOPS                         |      |   827K|  1773M|   111   (0)| 00:00:01 |
|   2 |   NESTED LOOPS                        |      |  1235K|  1773M|   111   (0)| 00:00:01 |
|   3 |    TABLE ACCESS BY INDEX ROWID BATCHED| A    |   100 |   109K|   111   (0)| 00:00:01 |
|*  4 |     INDEX RANGE SCAN                  | A_A5 |   100 |       |     1   (0)| 00:00:01 |
|*  5 |    INDEX RANGE SCAN                   | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|   6 |   TABLE ACCESS BY INDEX ROWID         | B    |  8278 |  9134K|     0   (0)| 00:00:01 |
----------------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   4 - access("A"."A5"=833
   5 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

Plan hash value: 4028436644
 
-------------------------------------------------------------------------------------
| Id  | Operation                    | Name | Rows  | Bytes | Cost (%CPU)| Time     |
-------------------------------------------------------------------------------------
|   0 | SELECT STATEMENT             |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   1 |  NESTED LOOPS                |      |   827K|  1773M|  3989   (1)| 00:00:01 |
|   2 |   NESTED LOOPS               |      |   115M|  1773M|  3989   (1)| 00:00:01 |
|*  3 |    TABLE ACCESS FULL         | A    |  9324 |     9M|  3989   (1)| 00:00:01 |
|*  4 |    INDEX RANGE SCAN          | B_FK | 12356 |       |     0   (0)| 00:00:01 |
|   5 |   TABLE ACCESS BY INDEX ROWID| B    |    89 |    98K|     0   (0)| 00:00:01 |
-------------------------------------------------------------------------------------
 
Predicate Information (identified by operation id):
---------------------------------------------------
 
   3 - filter("A"."A6"=1
   4 - access("AK"="FAK"
 
Note
-----
   - dynamic statistics used: dynamic sampling (level=2

