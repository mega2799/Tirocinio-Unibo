from ast import expr_context
import random
from tqdm import tqdm
import csv
import xlsxwriter


expA = 1

expB = 2

N_A = 10**expA 

N_B = 10**expB

A = list(range(0, N_A))

B = list(range(0, N_B))

N_A1 = N_A/10

N_A2 = N_A/10**(round(expA/2))

N_A3 = N_A/10**(expA - 1)

N_B1 = N_B/10

N_B2 = N_B/10**(round(expB/2))

N_B3 = N_B/10**(expB - 1)

A1 = list(range(0, int(N_A1)))

A2 = list(range(0, int(N_A2)))

A3 = list(range(0, int(N_A3)))

B1 = list(range(0,int(N_B1)))

B2 = list(range(0,int(N_B2)))

B3 = list(range(0,int(N_B3)))

def populateList(rangeList):
    return list(range(0, int(rangeList)))

def getAndDel(array):
    if len(array) != 0:
        element = random.choice(array)
        ind = array.index(element)
        return array.pop(ind)
    else:
        return "pythonSucks"
        
tt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis."
t = ()
s = ()

if __name__ == "__main__":
   # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)

    # Insert an image.
    worksheet.insert_image('B5', 'logo.png')

    workbook.close() 


    # with open('framework_dict.csv', mode='w', newline='') as csv_file:
        # colonne = ['Nome', 'Linguaggio', 'Utilizzo(%)']
        # writer = csv.DictWriter(csv_file, fieldnames=colonne)
# 
        # writer.writeheader()
        # writer.writerow({'Nome': 'Django', 'Linguaggio': 'Python', 'Utilizzo(%)': 40})
        # writer.writerow({'Nome': 'Blazor', 'Linguaggio': 'C#', 'Utilizzo(%)': 20})
        # writer.writerow({'Nome': 'NodeJS', 'Linguaggio': 'Javascript', 'Utilizzo(%)': 60})

    exit(0)
    file_A = open("data.sql", "w")
    file_A.write(
        "Create table A( " + "\n" +
        "A_AK NUMBER(6,0), " +   "\n" +
        "A_A1 NUMBER(6,0), " +   "\n" +
        "A_A2 NUMBER(6,0), " +   "\n" +
        "A_A3 NUMBER(6,0), " +   "\n" +
        "A_A4 NUMBER(6,0), " +   "\n" +
        "A_A5 NUMBER(6,0), " +   "\n" +
        "A_A6 NUMBER(6,0), " +   "\n" +
        "A_A7 VARCHAR(1005), " + "\n" +
        "PRIMARY KEY(A_AK));" + "\n"
    )
    file_A.write(
        "\n" + "Create table B( " + "\n" +
        "B_BK NUMBER(6,0), " +   "\n" +
        "B_AK NUMBER(6,0), " +   "\n" +
        "B_B1 NUMBER(6,0), " +   "\n" +
        "B_B2 NUMBER(6,0), " +   "\n" +
        "B_B3 NUMBER(6,0), " +   "\n" +
        "B_B4 NUMBER(6,0), " +   "\n" +
        "B_B5 NUMBER(6,0), " +   "\n" +
        "B_B6 NUMBER(6,0), " +   "\n" +
        "B_B7 VARCHAR(1005), " + "\n" +
        "PRIMARY KEY(B_BK), " + "\n"
        "FOREIGN KEY(B_AK) REFERENCES A(A_AK));" +          "\n"
    )
    for j in range(4):
        t = ()
        s = ()
        for i in tqdm(range(int(N_A/4))):
            AK = getAndDel(A)
            el_A1 = getAndDel(A1)
            if el_A1 == "pythonSucks":
                A1 = populateList(N_A1)
                el_A1 = getAndDel(A1) 
            el_A2 = getAndDel(A2)
            if el_A2 == "pythonSucks":
                A2 = populateList(N_A2)
                el_A2 = getAndDel(A2) 
            el_A3 = getAndDel(A3)
            if el_A3 == "pythonSucks":
                A3 = populateList(N_A3)
                el_A3 = getAndDel(A3) 
            t += ((AK, el_A1, el_A2, el_A3, el_A1, el_A2, el_A3, tt),)
            for y in range(10):
                BK = getAndDel(B)
                el_B1 = getAndDel(B1)
                if el_B1 == "pythonSucks":
                    B1 = populateList(N_B1)
                    el_B1 = getAndDel(B1)
                el_B2 = getAndDel(B2)
                if el_B2 == "pythonSucks":
                    B2 = populateList(N_B2)
                    el_B2 = getAndDel(B2)
                el_B3 = getAndDel(B3)
                if el_B3 == "pythonSucks":
                    B3 = populateList(N_B3)
                    el_B3 = getAndDel(B3)
                s += ((BK, AK, el_B1, el_B2, el_B3, el_B1, el_B2, el_B3, tt),)
        file_A.write("INSERT INTO A VALUES ")
        file_A.write(str(t) + ";\n\n")
        file_A.write("\nINSERT INTO B VALUES ")
        file_A.write(str(s)+ ";\n\n")