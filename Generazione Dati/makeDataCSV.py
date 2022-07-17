from ast import expr_context
import random
from tqdm import tqdm
import csv
import xlsxwriter


expA = 5

expB = 6

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
   ## Create an new Excel file and add a worksheet.
   # workbook = xlsxwriter.Workbook('demo.xlsx')
   # worksheet = workbook.add_worksheet()

   # # Widen the first column to make the text clearer.
   # worksheet.set_column('A:A', 20)

   # # Add a bold format to use to highlight cells.
   # bold = workbook.add_format({'bold': True})

   # # Write some simple text.
   # worksheet.write('A1', 'Hello')

   # # Text with formatting.
   # worksheet.write('A2', 'World', bold)

   # # Write some numbers, with row/column notation.
   # worksheet.write(2, 0, 123)
   # worksheet.write(3, 0, 123.456)

   # # Insert an image.
   # worksheet.insert_image('B5', 'logo.png')

   # workbook.close() 


    with open('A.csv', mode='w', newline='') as csv_file:
        colonne = ['AK', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
        writerA = csv.DictWriter(csv_file, fieldnames=colonne)

        writerA.writeheader()
        # writer.writerow({'Nome': 'Blazor', 'Linguaggio': 'C#', 'Utilizzo(%)': 20})
        # writer.writerow({'Nome': 'NodeJS', 'Linguaggio': 'Javascript', 'Utilizzo(%)': 60})
        with open('B.csv', mode='w', newline='') as csv_fileB:
            colonne = ['BK', 'FAK','B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
            writerB = csv.DictWriter(csv_fileB, fieldnames=colonne)

            writerB.writeheader()

            for i in tqdm(range(N_A)):
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
                writerA.writerow({"AK" : AK,"A1" : el_A1, "A2" : el_A2, "A3" : el_A3, "A4" : el_A1, "A5" : el_A2,"A6" : el_A3 , "A7" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis." }) 
                for y in range(10):
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
                    writerB.writerow({"BK" : getAndDel(B), "FAK" : AK, "B1" : el_B1, "B2" : el_B2, "B3" : el_B3, "B4" : el_B1, "B5" : el_B2, "B6" : el_B3 , "B7" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis." })