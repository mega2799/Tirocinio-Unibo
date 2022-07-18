import json
import numpy as np
import os 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import xlsxwriter
import csv

data = np.zeros(shape=(4, 12), dtype=int)
#data = {}
barWidth = 0.25

times = []
collection = []
colls = []
indexes = []

get_rowNum = {'embedding_A_in_B' : 0,'embedding_B_in_A' : 1,'referencing_B_in_A' : 2,'referencing_A_in_B' : 3}
get_colNum = {'A1' : 0,'A2' : 1,'A3' : 2,'A4' : 3, 'A5' : 4, 'A6' : 5, 'B1' : 6,'B2' : 7,'B3' : 8,'B4' : 9, 'B5' : 10, 'B6' : 11}


files = os.listdir("../result/")
#files = [file[:-5] for file in files]

workbook = xlsxwriter.Workbook('MongoDBStat.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.set_column(1, 1, 20)
worksheet.set_column(2, 2, 20)
worksheet.set_column(3, 3, 20)
worksheet.set_column(4, 4, 20)

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

worksheet.write_string('B1', 'embedding_A_in_B', bold)
worksheet.write_string('C1', 'embedding_B_in_A', bold)
worksheet.write_string('D1', 'referencing_A_in_B', bold)
worksheet.write_string('E1', 'referencing_A_in_B', bold)


#worksheet.write_string('A2', 'embedding_A_in_B', bold)
#worksheet.write_string('A3', 'embedding_B_in_A', bold)
#worksheet.write_string('A4', 'referencing_A_in_B', bold)
#worksheet.write_string('A5', 'referencing_A_in_B', bold)

#worksheet.write_string('B1', 'A1', bold)
#worksheet.write_string('C1', 'A2', bold)
#worksheet.write_string('D1', 'A3', bold)
#worksheet.write_string('E1', 'A4', bold)
#worksheet.write_string('F1', 'A5', bold)
#worksheet.write_string('G1', 'A6', bold)
#worksheet.write_string('H1', 'B1', bold)
#worksheet.write_string('I1', 'B2', bold)
#worksheet.write_string('J1', 'B3', bold)
#worksheet.write_string('K1', 'B4', bold)
#worksheet.write_string('L1', 'B5', bold)
#worksheet.write_string('M1', 'B6', bold)

for file in files:
    if "exec_stats" in file:
        name = "../result/" + file
        with open(name, "r") as file:
            j = json.load(file)
        if "stages" in list(j.keys()):
            time = (j["stages"][0]["$cursor"]["executionStats"]["executionTimeMillis"])
        else:
            time = (j["executionStats"]["executionTimeMillis"])
        #print(name, time)
        splitted = (name.split("@"))
        collection= (splitted[0].split('/')[2])
        colls.append(collection)
        ind = (splitted[1])
        data[get_rowNum[collection], get_colNum[ind]] = time
        worksheet.write(get_colNum[ind] + 1, get_rowNum[collection] + 1 , time)

workbook.close() 
#print(data)


exit(0)
#[data.get(x) for x in collections] 
collections = data.keys()
for i in ([y for y in [data.get(x) for x in collections]]):
    for ind in i:
        indexes.append(list(ind.keys())[0])

for arr in [data.get(x) for x in collections]:
    for val in arr:
        times.append(list(val.values())[0])

#t = np.array_split(np.array(times), 4)
#idx = np.array_split(np.array(indexes), 4)
#
#left = [1, 2, 3, 4, 5, 6]
#
#for b in range(len(t)):
#    plt.bar(left, t[b], tick_label = idx[b],
#        width = 0.8, color = ['red', 'green'])
#
#plt.show()

t = np.array(times)
idx = np.array(indexes)

print(t, idx)
#left = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
left = np.arange(1, len(t) + 1, 1)

def add_value_label(x_list,y_list):
    for i in range(1, len(x_list)+1):
        plt.text(i,y_list[i-1],str(y_list[i-1]), ha = 'center')

barlist = plt.bar(left, t, tick_label = idx, 
        width = 0.6)

#plt.xlabel(t)
#plt.text(left, t, t)
add_value_label(t, t)
#plt.xlabel('referencing_A_in_B  referencing_B_in_A    embedding_B_in_A     embedding_A_in_B')

colors = ['r', 'b', 'g', 'y']

for color, bar_group in zip(colors, np.array_split(barlist, 4)):
    for bar in bar_group:
        bar.set_color(color)

red_patch = mpatches.Patch(color='red', label='embedding_A_in_B')
blu_patch = mpatches.Patch(color='b', label='referencing_B_in_A')
green_patch = mpatches.Patch(color='g', label='referencing_A_in_B')
yellow_patch = mpatches.Patch(color='y', label='embedding_B_in_A')
plt.legend(handles=[red_patch, blu_patch, green_patch, yellow_patch])

plt.show()







#br1 = np.arange(len(colls))
#br2 = [x + barWidth for x in br1]
#br3 = [x + barWidth for x in br2]

#plt.bar(br1, colls, color ='r', width = barWidth,
#        edgecolor ='grey', label ='IT')
#plt.bar(br2, indexes , color ='g', width = barWidth,
#        edgecolor ='grey', label ='ECE')
#plt.bar(br3, times, color ='b', width = barWidth,
#        edgecolor ='grey', label ='CSE')

#plt.legend()
#plt.show()
