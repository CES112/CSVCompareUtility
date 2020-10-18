import csv

standardFile = open('test_csvs/orig-file.csv')
csvStandard= csv.reader(standardFile)

compColumn=0
for c in csvStandard:
    #print(c[valuuu])
    comparisonFile = open('test_csvs/compfile.csv')
    csvCompare = csv.reader(comparisonFile)
    for row in csvCompare:
        if row[compColumn]==c[compColumn]:
            print("match:"+ row[compColumn])
            break
        else:
            print("no match")

    comparisonFile.close()
standardFile.close()