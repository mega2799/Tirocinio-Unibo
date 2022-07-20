from random import randint
import cx_Oracle
import config
import time
import xlsxwriter

connection = None
ind_a= ["A1",  "A2",  "A3",  "A4",  "A5", "A6"]

ind_b= ["B1",  "B2",  "B3",  "B4",  "B5", "B6"]

get_rowNum = {'A' : 0,'B' : 1}
get_colNum = {'A1' : 0,'A2' : 1,'A3' : 2,'A4' : 3, 'A5' : 4, 'A6' : 5, 'B1' : 6,'B2' : 7,'B3' : 8,'B4' : 9, 'B5' : 10, 'B6' : 11}
get_colNumj = {'A1' : 12,'A2' : 13,'A3' : 14,'A4' : 15, 'A5' : 16, 'A6' : 17, 'B1' : 18,'B2' : 19,'B3' : 20,'B4' : 21, 'B5' : 22, 'B6' : 23}
workbook = xlsxwriter.Workbook('OracleStat.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write_string('B1', 'A', bold)
worksheet.write_string('C1', 'B', bold)

worksheet.write_string('A2', 'A1', bold)
worksheet.write_string('A3', 'A2', bold)
worksheet.write_string('A4', 'A3', bold)
worksheet.write_string('A5', 'A4', bold)
worksheet.write_string('A6', 'A5', bold)
worksheet.write_string('A7', 'A6', bold)
worksheet.write_string('A8', 'B1', bold)
worksheet.write_string('A9', 'B2', bold)
worksheet.write_string('A10', 'B3', bold)
worksheet.write_string('A11', 'B4', bold)
worksheet.write_string('A12', 'B5', bold)
worksheet.write_string('A13', 'B6', bold)
worksheet.write_string('A14' , 'A1j', bold)
worksheet.write_string('A15' , 'A2j', bold)
worksheet.write_string('A16' , 'A3j', bold)
worksheet.write_string('A17' , 'A4j', bold)
worksheet.write_string('A18' , 'A5j', bold)
worksheet.write_string('A19' , 'A6j', bold)
worksheet.write_string('A20' , 'B1j', bold)
worksheet.write_string('A21' , 'B2j', bold)
worksheet.write_string('A22' , 'B3j', bold)
worksheet.write_string('A23' , 'B4j', bold)
worksheet.write_string('A24' , 'B5j', bold)
worksheet.write_string('A25' , 'B6j', bold)

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
            # rows = cursor.fetchall()
            # print('rows: ', len(rows))
                    # worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            # rows = cursor.fetchall()
        collection = "B"
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
            # rows = cursor.fetchall()
            # print('rows: ', len(rows))
        ## JOIN QUERIES
        sttt = "select A.*, B.* from A join B on (AK = FAK) where "
        collection = "A"
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
            print('rows: ', len(rows))
                    # worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , int(t))
            # rows = cursor.fetchall()
        collection = "B"
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
            print('rows: ', len(rows))
        connection.close()
        workbook.close() 