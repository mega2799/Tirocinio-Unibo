from random import randint
import cx_Oracle
import config
import time
import xlsxwriter

connection = None
ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]

ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

#get_rowNum = {'A' : 0,'B' : 1}
get_rowNum = {'A ' : 0,'B ' : 1}
get_colNum = {
'A0' : 0,
'A1' : 1,
'A2' : 2,
'A3' : 3,
'A4' : 4,
'A5' : 5,
'A6' : 6,
'B0' : 7,
'B1' : 8,
'B2' : 9,
'B3' : 10,
'B4' : 11,
'B5' : 12,
'B6' : 13
}

workbook = xlsxwriter.Workbook('OracleStatUpdate.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.write_string('B1', 'A', bold)
worksheet.write_string('C1', 'B', bold)
worksheet.write_string('A2', 'A0', bold)
worksheet.write_string('A3', 'A1', bold)
worksheet.write_string('A4', 'A2', bold)
worksheet.write_string('A5', 'A3', bold)
worksheet.write_string('A6', 'A4', bold)
worksheet.write_string('A7', 'A5', bold)
worksheet.write_string('A8', 'A6', bold)
worksheet.write_string('A9', 'B0', bold)
worksheet.write_string('A10', 'B1', bold)
worksheet.write_string('A11', 'B2', bold)
worksheet.write_string('A12', 'B3', bold)
worksheet.write_string('A13', 'B4', bold)
worksheet.write_string('A14', 'B5', bold)
worksheet.write_string('A15', 'B6', bold)

try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
finally:
    if connection:
        file_A = open("A_update.sql", "w")
        file_B = open("B_update.sql", "w")
        expl = "EXPLAIN PLAN FOR "
        print_expl = "SELECT PLAN_TABLE_OUTPUT FROM TABLE(DBMS_XPLAN.DISPLAY())"
        print("connected")
        cursor = connection.cursor()
        collection = "A "
        # cursor.execute("EXPLAIN PLAN SET statement_id = 'ex_plan2' FOR select * from A where A5 = 123;")
        # "SELECT PLAN_TABLE_OUTPUT FROM TABLE(DBMS_XPLAN.DISPLAY(NULL, 'ex_plan2','BASIC'));")
        # AK
        start_time = time.time()
        cursor.execute(expl + "update " + collection + "set A7= 14 where AK = " + str(randint(0,9999)))
        t = (time.time() - start_time)
        t *= 1000
        cursor.execute(print_expl)
        # file_A.write(str([ str(x) + "\n" for x in cursor.fetchall()]))
        # file_A.write(str(["\n".join(x) for x in cursor.fetchall()]))

        # NON VUOLE ANDARE A CAPO !
        # print(str(['\n'.join(x) for x in cursor.fetchall()]).strip('[]'))
        for x in cursor.fetchall():
            file_A.write(str(x).strip('(),\''))
            file_A.write('\n')
        worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1 , int(t))
        for ind in ind_a:
            match ind:
                case 'A1':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set A7= 14 where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_A.write(str(x).strip('(),\''))
                        file_A.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A2':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set A7= 14 where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_A.write(str(x).strip('(),\''))
                        file_A.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A3':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set A7= 14 where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_A.write(str(x).strip('(),\''))
                        file_A.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A4':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set A7= 14 where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_A.write(str(x).strip('(),\''))
                        file_A.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A5':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set A7= 14 where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_A.write(str(x).strip('(),\''))
                        file_A.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A6':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set A7= 14 where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_A.write(str(x).strip('(),\''))
                        file_A.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            # rows = cursor.fetchall()
            # print('rows: ', len(rows))
                    # worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            # rows = cursor.fetchall()
        collection = "B "
        # AK
        start_time = time.time()
        cursor.execute(expl + "update " + collection + "set B7= 14 where BK = " + str(randint(0,9999)))
        t = (time.time() - start_time)
        t *= 1000
        cursor.execute(print_expl)
        for x in cursor.fetchall():
            file_B.write(str(x).strip('(),\''))
            file_B.write('\n')
        worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1 , int(t))
        rows = cursor.fetchall()
        print('prim key rows: ', len(rows))
        for ind in ind_b:
            match ind:
                case 'B1':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set B7= 14 where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_B.write(str(x).strip('(),\''))
                        file_B.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B2':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set B7= 14 where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_B.write(str(x).strip('(),\''))
                        file_B.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B3':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set B7= 14 where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_B.write(str(x).strip('(),\''))
                        file_B.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B4':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set B7= 14 where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_B.write(str(x).strip('(),\''))
                        file_B.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B5':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set B7= 14 where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_B.write(str(x).strip('(),\''))
                        file_B.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B6':
                    start_time = time.time()
                    cursor.execute(expl + "update " + collection + "set B7= 14 where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    cursor.execute(print_expl)
                    for x in cursor.fetchall():
                        file_B.write(str(x).strip('(),\''))
                        file_B.write('\n')
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
        connection.close()
        workbook.close() 