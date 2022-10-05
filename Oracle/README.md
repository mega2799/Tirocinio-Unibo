# Oracle

Importa i file .csv con oracle.

Potrebbe essere importante creare prima gli indici e le chiavi primarie

A

```sql
CREATE TABLE "C##TIROCINIO"."A" 
   ( "AK" NUMBER(38,0) NOT NULL ENABLE, 
 "A1" NUMBER(38,0), 
 "A2" NUMBER(38,0), 
 "A3" NUMBER(38,0), 
 "A4" NUMBER(38,0), 
 "A5" NUMBER(38,0), 
 "A6" NUMBER(38,0), 
 "A7" VARCHAR2(2048 BYTE), 
  CONSTRAINT "PK" PRIMARY KEY ("AK"));
```

B

```sql
 CREATE TABLE "C##TIROCINIO"."B" 
   ( "BK" NUMBER(38,0) NOT NULL ENABLE, 
 "FAK" NUMBER(38,0), 
 "B1" NUMBER(38,0), 
 "B2" NUMBER(38,0), 
 "B3" NUMBER(38,0), 
 "B4" NUMBER(38,0), 
 "B5" NUMBER(38,0), 
 "B6" NUMBER(38,0), 
 "B7" VARCHAR2(2048 BYTE), 
  CONSTRAINT "PKB" PRIMARY KEY ("BK"));
```

Primary key per A

```sql
alter table "A" add constraint PK primary key("AK") 
```

Primary key per B

```sql
alter table "B" add constraint PKB primary key("BK") 
```

Aggiungere il constraint per FAK

```sql
ALTER TABLE B
  ADD CONSTRAINT FK_A_constr FOREIGN KEY (FAK)     
      REFERENCES A(AK)
      ON DELETE CASCADE;
```

Indici

```sql
CREATE UNIQUE INDEX A_AK ON A (AK ASC);
CREATE INDEX A_A4 ON A (A4 ASC);
CREATE INDEX A_A5 ON A (A5 ASC);
CREATE INDEX A_A6 ON A (A6 ASC);
CREATE UNIQUE INDEX B_BK ON B (BK ASC);
CREATE INDEX B_B4 ON B (B4 ASC);
CREATE INDEX B_B5 ON B (B5 ASC);
CREATE INDEX B_B6 ON B (B6 ASC);
CREATE INDEX B_FK ON B (FAK ASC);
```

Ridurre la cache del client di sistema

```sql
ALTER SYSTEM SET CLIENT_RESULT_CACHE_SIZE = 128M SCOPE=SPFILE;
```
