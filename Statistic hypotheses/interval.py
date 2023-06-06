import csv
import matplotlib.pyplot as plt
import os

if os.name == 'nt':

    path = 'C:/Users/Oleh/Documents/GitHub/Statistic/Images/'
if os.name == 'posix':
    path = '/Users/olegvojtovic/Desktop/Statistic/Images/'


def makeBar(intervalDict, filename):
    internalDict = {}
    for key, value in intervalDict.items():
        if isinstance(key, tuple):
            internalDict[str(f"{key[0]} - {key[1]}")] = value
        else:
            internalDict[str(key)] = value

    plt.subplots(figsize=(len(internalDict.keys()) * 2, len(internalDict.values())))
    plt.bar(internalDict.keys(), internalDict.values())
    plt.yticks(list(internalDict.values()))
    plt.grid(True)
    plt.savefig(path + filename, bbox_inches='tight')


def makePoligon(intervalDict, filename):
    centralDict = {}
    for key, value in intervalDict.items():
        if isinstance(key, tuple):
            centralDict[int((key[0] + key[1]) / 2)] = int(value)
        else:
            centralDict[int(key)] = int(value)

    plt.figure(figsize=(len(intervalDict.keys()) * 2, len(intervalDict.values())))
    plt.subplot(133)
    plt.plot(list(centralDict.keys()), list(centralDict.values()))
    plt.grid(True)
    plt.savefig(path + filename, bbox_inches='tight')


def makeStartExerciseCSV(filename, mode):
    intervalDict = {}
    if mode == 1:
        n = [4, 9, 28, 48, 70, 72, 52, 22, 10, 6]
        x = []
        for i in range(170, 280, 10):
            x.append(i)

        for i in range(0, len(x) - 1):
            intervalDict[f"{x[i]}-{x[i + 1]}"] = n[i]
    if mode == 2:
        n = [518, 392, 284, 205, 156, 120, 86, 61, 44, 34]
        x = []
        for i in range(0, 60, 6):
            x.append(i)

        for i in range(0, len(x) - 1):
            intervalDict[f"{x[i]}-{x[i + 1]}"] = n[i]
        intervalDict[x[-1]] = n[-1]

    with open(path + filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(intervalDict.keys())
        w.writerow(intervalDict.values())


def makeNewDataFile(intervalDict, filename):
    with open(path + filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(intervalDict.keys())
        w.writerow(intervalDict.values())


def readCSV(filename):
    with open(path + filename, 'r') as data:
        dict_reader = csv.DictReader(data)
        temp = list(dict_reader)

    tempDict = temp[0]
    finalDict = {}
    for i in tempDict.items():
        if '-' in i[0]:
            key = [float(i) for i in i[0].split('-')]
            key.sort()
            finalDict[(key[0], key[1])] = int(i[1])
        else:
            finalDict[float(i[0])] = int(i[1])
    return finalDict
