import csv
import os
import time

def selectComparisonColumn (selectedFile):
    fieldOptionCount=1
    with open(selectedFile, newline='') as f:
        headerReader = csv.DictReader(f)
        fileHeaders = headerReader.fieldnames
        for fheader in fileHeaders:
            print(str(fieldOptionCount) + ': ' + fheader)
            fieldOptionCount+=1
    
        selectedColumn = int(input("Select comparison column for the first file:"))
        selectedColumn -= 1
        print(fileHeaders[selectedColumn]) 
        print(str(selectedColumn))
    f.close()
    return selectedColumn


firstFile = input("Enter the location and filename of the first file:")
compColumn1 = selectComparisonColumn(firstFile)

secFile = input("Enter the location and filename of the second file:")
compColumn2 = selectComparisonColumn(secFile)


standardFile = open (firstFile)
csvStandard= csv.reader(standardFile)

timeStampString=time.strftime("%Y%m%d-%H%M%S")
tempCompareFileName=('temp-compare-'+timeStampString)
print(tempCompareFileName)
os.system("cp "+secFile +" "+tempCompareFileName)

compColumn=0
for c in csvStandard:

    comparisonFile = open(tempCompareFileName)
    csvCompare = csv.reader(comparisonFile)
    for row in csvCompare:
        if c[compColumn1]==row[compColumn2]:
            print("match:"+ row[compColumn2])
            break
        else:
            print("no match")

    comparisonFile.close()
standardFile.close()

tempRemoveFlag = input("Enter anything:")
os.remove(tempCompareFileName)