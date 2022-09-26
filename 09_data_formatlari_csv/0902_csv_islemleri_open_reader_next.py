# region csv_giris
"""
import csv
with open("xvericom-v1.csv", "r", encoding="utf-8") as csvFile:
     print(csvFile.read())
     cReader = csv.reader(csvFile)
     #print(cReader)
#print(type(cReader))
print(list(cReader))
#for row in cReader:
# print(row)
    
    """ 
# endregion

import csv
with open("devices.csv", "r", encoding="utf-8") as csvFile:
    cReader = csv.reader(csvFile)
    for row in cReader:
        print(row)
       # print(row[0], row[2])
        #if row[2] == "router":
            #print(row)
            #print(f"device name: {row[0]} ip address: {row[2]} ")


