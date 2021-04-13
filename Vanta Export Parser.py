#   Vanta Export Parser v0.1 by ZH (13/04/2021)

import csv

global headerOrder
global headerIndexes
global currentRowData
global rowCount
headerOrder = ["Reading #","Instrument Serial Num","Date","Time","Method Name"]
headerIndexes = []
currentRowData = []
rowCount = 0



def getInput():                             # Gets user input and fills related variables accordingly

    global exportName
    exportName = input("Vanta Export file name (including extension, e.g. chemistry-800151-2021-03-17-12-22-21.csv):")
    print("Formatting", exportName, "to output.csv")


def getColumnIndex(columnHeader):           # Gets the index number of the column named in the input
    with open(exportName) as exportFile:
        reader = csv.reader(exportFile)
        for row in reader:
            for k,v in enumerate(row):
                if v == columnHeader:
                    return k

def getRowCount():
    with open(exportName) as exportFile:
        reader = csv.reader(exportFile)
        rowCount = sum(1 for row in reader)

def fillData():
    for i in 



def writeCSV():                             # Writes data in outputArray to output.csv
    with open('output.csv', mode='w') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(outputArray)
    print("output.csv was written successfully.")




getInput()
for header in headerOrder:                              # fills headerIndexes list with the indexes of the headers specified in headerOrder, for easy parsing of future rows
    try:
        headerIndexes.append(getColumnIndex(header))    # try to find header index if such header exists in file
    except:
        headerIndexes.append(999)                       # if no such header found, list position filled with 999, which will give an index error later.





writeCSV()
input("Press Enter to continue...")

    

