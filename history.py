import os
import json

files = os.listdir("sermons")
#print(files)
folder = input("folder: ")
fopen = open("history.json", "r")
jsondata = json.loads(fopen.read())
fopen.close()
jsondata[folder]= {}
for f in files:
    if f.endswith("mp4"):
        jsondata[folder][f]  = {"visited": False}

print(jsondata)        
with open("history.json", "w", encoding="utf-8") as file:
    json.dump(jsondata, file, indent=4)        

        