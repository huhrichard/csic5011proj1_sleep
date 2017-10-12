import sys
import pandas as pd
import numpy as np
import csv

def readCSVbyPandas(csvFile):
    df = pd.read_csv(csvFile, sep=',')
    data = df.values
    # print data[0][0]
    columnWithoutNan = range(data[0].shape[0]);
    for animal in data:
        # pd.isnull(animal)[0]
        for idx in range(data[0].shape[0]):
            if idx in columnWithoutNan:
                if pd.isnull(animal[idx]) == True:
                    columnWithoutNan.remove(idx)
    return df, columnWithoutNan

# def readCSV(csvFile):
#     animalList = []
#     columnWithNan = []
#     with open(csvFile, 'r') as csvin:
#         csvreader = csv.reader(csvin, delimiter=',')
#         for line in csvreader:
#             animal = []
#             for idx, item in enumerate(line):
#                 if idx not in columnWithNan:
#                     if item == 'NA':
#                         columnWithNan.append(idx)
#                 animal.append(item)
#             animalList.append(animal)
#     return animalList, columnWithNan

def filterNan(df, columnWithoutNan):
    data = df.values
    filteredData = np.array([animal[columnWithoutNan[1:]] for animal in data])
    print filteredData
    return filteredData

def main(argv):
    df, columnWithoutNan = readCSVbyPandas(argv[-1])
    filteredData = filterNan(df, columnWithoutNan)

if __name__ == '__main__':
    main(sys.argv)