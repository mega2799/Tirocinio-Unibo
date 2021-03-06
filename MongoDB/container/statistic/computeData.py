import json
import numpy as np
import os 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#data = numpy.zeros(shape=(4, 6), dtype=int)
data = {}
barWidth = 0.25

times = []
collection = []
colls = []
indexes = []

files = os.listdir("../result/")
#files = [file[:-5] for file in files]
for file in files:
    if "exec_stats" in file:
        name = "../result/" + file
        with open(name, "r") as file:
            j = json.load(file)
        #for key, value in j.items():
        #    print("----" ,key, "--->", value)
        #print(j.get('stages'))
        #print(j["$cursor"]["executionStats"]["executionTimeMillis"])
        #time = (j["$cursor"]["executionStats"]["executionTimeMillis"])
        if "stages" in list(j.keys()):
            time = (j["stages"][0]["$cursor"]["executionStats"]["executionTimeMillis"])
        else:
            time = (j["executionStats"]["executionTimeMillis"])
        print(name, time)
        splitted = (name.split("@"))
        collection= (splitted[0].split('/')[2])
        colls.append(collection)
        ind = (splitted[1])
        data.setdefault(collection, [])
        data[collection].append({ind : time})

print(data)

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
