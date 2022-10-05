from random import randint
import cx_Oracle
import config
import time
import xlsxwriter

connection = None
ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]

ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

get_rowNum = {'A' : 0,'B' : 1}
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
get_colNumj = {
'A0' : 14,
'A1' : 15,
'A2' : 16,
'A3' : 17,
'A4' : 18,
'A5' : 19,
'A6' : 20,
'B0' : 21,
'B1' : 22,
'B2' : 23,
'B3' : 24,
'B4' : 25,
'B5' : 26,
'B6' : 27}

workbook = xlsxwriter.Workbook('OracleStat.xlsx')
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
worksheet.write_string('A16' , 'A0j', bold)
worksheet.write_string('A17' , 'A1j', bold)
worksheet.write_string('A18' , 'A2j', bold)
worksheet.write_string('A19' , 'A3j', bold)
worksheet.write_string('A20' , 'A4j', bold)
worksheet.write_string('A21' , 'A5j', bold)
worksheet.write_string('A22' , 'A6j', bold)
worksheet.write_string('A23' , 'B0j', bold)
worksheet.write_string('A24' , 'B1j', bold)
worksheet.write_string('A25' , 'B2j', bold)
worksheet.write_string('A26' , 'B3j', bold)
worksheet.write_string('A27' , 'B4j', bold)
worksheet.write_string('A28' , 'B5j', bold)
worksheet.write_string('A29' , 'B6j', bold)

try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # show the version of the Oracle Database
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        print("connected")
        cursor = connection.cursor()
        collection = "A"
        start_time = time.time()
        cursor.execute("select * from A where AK = " + str(randint(0,9999)))
        t = (time.time() - start_time)
        t *= 1000
        rows = cursor.fetchall()
        print('rows: ', len(rows))
        print('time: ', t)
        worksheet.write(get_colNum["A0"] + 1, get_rowNum[collection] + 1 , int(t))
        for ind in ind_a:
            match ind:
                case 'A1':
                    start_time = time.time()
                    cursor.execute("select * from A where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A2':
                    start_time = time.time()
                    cursor.execute("select * from A where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A3':
                    start_time = time.time()
                    cursor.execute("select * from A where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A4':
                    start_time = time.time()
                    cursor.execute("select * from A where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A5':
                    start_time = time.time()
                    cursor.execute("select * from A where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A6':
                    start_time = time.time()
                    cursor.execute("select * from A where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            rows = cursor.fetchall()
            print(ind)
            print('rows: ', len(rows))
            print('time: ', t)
                    # worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            # rows = cursor.fetchall()
        collection = "B"
        start_time = time.time()
        cursor.execute( "select * from B where BK = " + str(randint(0,9999)))
        t = (time.time() - start_time)
        t *= 1000
        worksheet.write(get_colNum["B0"] + 1, get_rowNum[collection] + 1 , int(t))
        rows = cursor.fetchall()
        print('rows: ', len(rows))
        print('time: ', t)
        for ind in ind_b:
            match ind:
                case 'B1':
                    start_time = time.time()
                    cursor.execute("select * from B where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B2':
                    start_time = time.time()
                    cursor.execute("select * from B where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B3':
                    start_time = time.time()
                    cursor.execute("select * from B where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B4':
                    start_time = time.time()
                    cursor.execute("select * from B where " + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B5':
                    start_time = time.time()
                    cursor.execute("select * from B where " + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B6':
                    start_time = time.time()
                    cursor.execute("select * from B where " + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            rows = cursor.fetchall()
            print(ind)
            print('rows: ', len(rows))
            print('time: ', t)
        ## JOIN QUERIES
        sttt = "select A.*, B.* from A join B on (AK = FAK) where "
        collection = "A"
        start_time = time.time()
        cursor.execute(sttt + " AK = " + str(randint(0,9999)))
        t = (time.time() - start_time)
        t *= 1000
        rows = cursor.fetchall()
        print('rows: ', len(rows))
        print('time: ', t)
        worksheet.write(get_colNumj["A0"] + 1, get_rowNum[collection] + 1 , int(t))
        for ind in ind_a:
            match ind:
                case 'A1':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A2':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A3':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A4':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A5':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'A6':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
            rows = cursor.fetchall()
            print('join ', ind)
            print('rows: ', len(rows))
            print('time: ', t)
                    # worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            # rows = cursor.fetchall()
        collection = "B"
        start_time = time.time()
        cursor.execute(sttt + " BK = " + str(randint(0,9999)))
        t = (time.time() - start_time)
        t *= 1000
        rows = cursor.fetchall()
        print('rows: ', len(rows))
        print('time: ', t)
        worksheet.write(get_colNumj["B0"] + 1, get_rowNum[collection] + 1 , int(t))
        for ind in ind_b:
            match ind:
                case 'B1':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B2':
                    start_time = time.time()
                    cursor.execute(sttt  + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B3':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B4':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,9999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B5':
                    start_time = time.time()
                    cursor.execute(sttt + ind + " = " + str(randint(0,999)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
                case 'B6':
                    start_time = time.time()
                    cursor.execute(sttt  + ind + " = " + str(randint(0,9)))
                    t = (time.time() - start_time)
                    t *= 1000
                    worksheet.write(get_colNumj[ind] + 1, get_rowNum[collection] + 1 , int(t))
            rows = cursor.fetchall()
            print('join ', ind)
            print('rows: ', len(rows))
            print('time:', t)

        connection.close()
        workbook.close() 
