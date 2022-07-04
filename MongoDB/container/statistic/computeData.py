import json
import os 

files = os.listdir("../result/")
#files = [file[:-5] for file in files]
for file in files:
    if "exec_stats" in file:
        print("../result/" + file)
        with open(("../result/" + file), "r") as r_file:
            j = json.load(r_file)
            print(j["executionStats"]["executionTimeMillis"])