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


def removeRow (tempFile, deleteLine):
    lineCount =0
    with open(tempFile, "r") as tF:
        lines = tF.readlines()
    with open(tempFile, "w") as tF:
        for line in lines:
            if (lineCount != deleteLine):
                tF.write(line)
            lineCount+=1
    

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


for c in csvStandard:
    compColumn=0
    comparisonFile = open(tempCompareFileName)
    csvCompare = csv.reader(comparisonFile)
    for row in csvCompare:
        compColumn +=1
        if c[compColumn1]==row[compColumn2]:
            print("match:"+ row[compColumn2])
            print("line: "+ str(compColumn))

    comparisonFile.close()
    removeRow (tempCompareFileName, (compColumn-1))


standardFile.close()

tempRemoveFlag = input("Enter anything:")
os.remove(tempCompareFileName)