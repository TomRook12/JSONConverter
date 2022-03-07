import pandas as pd
import os

d = {"participant":
         [],
     "affiliation":
         [],
     "time/distance":
         [],
     "avg_pace":
         [],
     "score":
         [],
     }

def json_opener(json_file):
    with open(json_file, encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)
    return(df)

def validity_checker(data,i):
    if data["results"]["participants"][i]["affiliation"] == "EMPT":
        return False
    if data['results']["participants"][i]["avg_pace"] == "0:00.0":
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
            d["time/distance"].append(data["results"]["duration"])
            d["avg_pace"].append(data['results']["participants"][i]["avg_pace"])
            d["score"].append(data["results"]["participants"][i]["score"])
    return d


files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    if f.endswith(".json"):
        table = pd.DataFrame.from_dict(result_creator(json_opener(f)))

table.to_csv("data.csv")

"""table = pd.DataFrame.from_dict(folder_reader(df))
print(table)

table.to_csv("data.csv")

"""

