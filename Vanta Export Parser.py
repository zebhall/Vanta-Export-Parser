#   Vanta Export Parser v1.0 by ZH (14/04/2021)

import csv

global headerOrder
global headerIndexes
global currentRowData
global currentRowDataRaw
#global rowCount
headerOrder = ["Instrument Serial Num","Test Label","Date","Time","Method ID","Test Status","Real Time 1","Real Time 2","Real Time 3","User Factor Name","Units","Al Concentration","Al Error1s","As Concentration","As Error1s","Fe Concentration","Fe Error1s","Rb Concentration","Rb Error1s","Ti Concentration","Ti Error1s","LE Concentration","LE Error1s"]
headerIndexes = []
currentRowData = []
currentRowDataRaw = []
#rowCount = 0



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


#def getRowCount():                          #Defunct function, unused.
#    with open(exportName) as exportFile:
#        reader = csv.reader(exportFile)
#        rowCount = sum(1 for row in reader)


def getHeaderIndexes():
    for header in headerOrder:                              # fills headerIndexes list with the indexes of the headers specified in headerOrder, for easy parsing of future rows
        try:
            headerIndexes.append(getColumnIndex(header))    # try to find header index if such header exists in file
        except:
            headerIndexes.append(999)                       # if no such header found, list position filled with 999, which will give an index error later.


def fillData():                                             # pulls data from file using header indexes then writes it to output.csv, one row at a time.
    with open('output.csv', mode='w', newline='') as outputFile:
        with open(exportName) as exportFile:
            writer = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            reader = csv.reader(exportFile)
            writer.writerow(headerOrder)
            for row in reader:
                for i in headerIndexes:
                    try:
                        currentRowData.append(row[i])
                    except:
                        currentRowData.append("")
                writer.writerow(currentRowData)
                currentRowData.clear()

#    r=0
#    while r>(rowCount+1):
#        currentRowData = []
#        currentRowDataRaw = []
#        with open(exportName) as exportFile:
#            reader = csv.reader(exportFile)



getInput()
getHeaderIndexes()
fillData()



input("Press Enter to continue...")

    

