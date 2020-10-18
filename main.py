import csv
import os
import time

firstFile = input("Enter the location and filename of the first file:")
secFile = input("Enter the location and filename of the second file:")

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
        if row[compColumn]==c[compColumn]:
            print("match:"+ row[compColumn])
            break
        else:
            print("no match")

    comparisonFile.close()
standardFile.close()

tempRemoveFlag = input("Enter anything:")
os.remove(tempCompareFileName)