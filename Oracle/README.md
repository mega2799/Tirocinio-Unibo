# Oracle

Importa i file .csv con oracle.

Potrebbe essere importante creare prima gli indici e le chiavi primarie

Primary key per A

```sql
alter table "SYS"."A" add constraint PK primary key("AK") 
```

Primary key per B

```sql
alter table "SYS"."B" add constraint PKB primary key("BK") 
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
CREATE BITMAP INDEX A_A3_BITMAP ON A (A3 ASC);
CREATE BITMAP INDEX A_A4_BITMAP ON A (A4 ASC);
CREATE BITMAP INDEX A_A5_BITMAP ON A (A5 ASC);
CREATE BITMAP INDEX B_B3_BITMAP ON B (B3 ASC);
CREATE BITMAP INDEX B_B4_BITMAP ON B (B4 ASC);
CREATE BITMAP INDEX B_B5_BITMAP ON B (B5 ASC);
```

Ridurre la cache del client di sistema

```sql
ALTER SYSTEM SET CLIENT_RESULT_CACHE_SIZE = 128M SCOPE=SPFILE;
```
