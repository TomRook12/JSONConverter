import pandas as pd
import os


'''with open('data.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)
'''
d = {"participant":
         [],
     "affiliation":
         [],
     "avg_pace":
         [],
     "score":
         [],
     }

def validity_checker(data,i):
    if data["results"]["participants"][i]["affiliation"] == "EMPT":
        return False
    if data["results"]["participants"][i]["machine_type"] != "row":
        return False
    else:
        return True

def result_creator(data):
    x = len(data["results"]["participants"])
    for i in range(0, x):
        if validity_checker(data, i):
            d["participant"].append(data["results"]["participants"][i]["participant"])
            d["affiliation"].append(data["results"]["participants"][i]["affiliation"])
            d["avg_pace"].append(data['results']["participants"][i]["avg_pace"])
            d["score"].append(data["results"]["participants"][i]["score"])
    return d

files = [f for f in os.listdir("JSON")]
print(files)
race = {}
for f in files:
    print(f)
    if f.endswith(".json"):
        with open(f, encoding='utf-8') as inputfile:
            df = pd.read_json(inputfile)
            print(df)









"""table = pd.DataFrame.from_dict(folder_reader(df))
print(table)

table.to_csv("data.csv")

"""

