import csv
import random
import math
import matplotlib.pyplot as plt

path = '/Users/olegvojtovic/Desktop/Python/Statistics/StatLab1/descrete'


def makePoligon(discreteDict, mode=None):
    if mode == 'relative':
        plt.figure(figsize=(max(discreteDict.keys()) + 5, max(discreteDict.values()) + 5))
        plt.subplot(133)
        plt.plot(list(discreteDict.keys()), list(discreteDict.values()))
        plt.savefig(path + 'relativeDiscretePoligon.jpg', bbox_inches='tight')
    else:
        plt.figure(figsize=(max(discreteDict.keys()), max(discreteDict.values())))
        plt.subplot(133)
        plt.plot(list(discreteDict.keys()), list(discreteDict.values()))
        plt.savefig(path + 'discretePoligon.jpg', bbox_inches='tight')


def plot_empirical_cdf(discreteDict, n):
    keyList = list(discreteDict.keys())
    vallist = YforEmpire(discreteDict, n)

    plt.subplots(figsize=(max(keyList),12))
    plt.grid(True)
    plt.yticks(vallist)
    for i in range(len(keyList)-1):
        plt.plot([keyList[i], keyList[i + 1]], [vallist[i], vallist[i]], c="blue")
    plt.xticks(keyList)
    plt.savefig(path + 'empire.jpg', bbox_inches='tight')


def YforEmpire(discreteDict, n):
    finallist = []
    valueList = list(discreteDict.values())

    for i in range(0, len(valueList)):
        temp = []
        for j in range(0, i):
            temp.append(valueList[j])

        finallist.append(temp)

    for i in range(0, len(finallist)):
        sum_n = 0
        for j in range(0, len(finallist[i])):
            sum_n += finallist[i][j]
        sum_n = sum_n / n
        finallist[i] = sum_n

    return finallist


def makeDiagram(discreteDict, filename):
    plt.figure(figsize=(9, 3))
    plt.stem(list(discreteDict.keys()), list(discreteDict.values()))
    plt.savefig(path + filename, bbox_inches='tight')


def makeFileCSV(discreteDict, filename):
    with open(path + filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(discreteDict.keys())
        w.writerow(discreteDict.values())


def numericalCharacteristics(discreteDict, n, filename):
    moments = moment(discreteDict, n, k=4)
    csvDict = {
        'мода': moda(discreteDict),
        'медіана': mediana(discreteDict),
        'с.а.': arithmeticMean(discreteDict, n),
        'розмах': swing(discreteDict),
        'девіація': dev(discreteDict, n),
        'варіанса': variance(discreteDict, n),
        'стандарт': standart(discreteDict, n),
        'варіація': variation(discreteDict, n),
        'дисперсія': dispersion(discreteDict, n),
        'c.квд.відхилення': meanSquareDeviation(discreteDict, n),
        'm1': moments[0],
        'm2': moments[1],
        'm3': moments[2],
        'm4': moments[3],
        'асиметрія': assymetry(moments[1], moments[2]),
        'ексцес': ecsess(moments[1], moments[3])

    }
    makeFileCSV(csvDict, filename)


# генеруєм вибрку заданого обєму для дискретної статистичної змінної та побудова варіаційного ряду і частотної таблиці
def discreteSample(n, a, b):
    sampleList = []
    for k in range(1, n):
        sampleList.append(random.randint(a, b))

    finalDictWithCounts = {}
    while len(sampleList) != 1:
        key = sampleList[0]
        value = sampleList.count(key)
        finalDictWithCounts[key] = value
        for j in range(0, len(sampleList) - 1):
            sampleList.remove(key)
            if sampleList.count(key) == 0:
                break

    Keys = list(finalDictWithCounts.keys())
    Keys.sort()
    finalDictWithCounts = {i: finalDictWithCounts[i] for i in Keys}
    return finalDictWithCounts


def relativeFrequencies(discreteDict, n):
    relativeDict = {}
    for key, value in discreteDict.items():
        relativeDict[key] = value / n

    return relativeDict


def moda(discreteDict):
    return max(discreteDict, key=lambda x: discreteDict[x])


def mediana(discreteDict):
    dicreteList = list(discreteDict)
    midIndex = int((len(dicreteList) / 2) - 1)
    if len(dicreteList) % 2 != 0:
        return dicreteList[midIndex]
    else:
        return (dicreteList[midIndex] + dicreteList[midIndex + 1]) / 2


def arithmeticMean(discreteDict, n):
    dicreteListKeys = list(discreteDict.keys())
    dicreteListValues = list(discreteDict.values())

    sum = 0
    for i in range(0, len(dicreteListKeys)):
        sum += dicreteListValues[i] * dicreteListKeys[i]

    return sum / n


def swing(discreteDict):
    discreteList = list(discreteDict.keys())
    x1 = int(discreteList[0])
    xn = int(discreteList[-1])
    return xn - x1


def dev(discreteDict, n):
    discreteList = list(discreteDict.keys())
    am = arithmeticMean(discreteDict, n)
    sum = 0
    for i in range(0, len(discreteList)):
        sum += (discreteList[i] - am) ** 2

    return sum


def variance(discreteDict, n):
    return (dev(discreteDict, n)) / (n - 1)


def standart(discreteDict, n):
    return math.sqrt(variance(discreteDict, n))


def variation(discreteDict, n):
    return (standart(discreteDict, n)) / arithmeticMean(discreteDict, n)


def dispersion(discreteDict, n):
    kys = list(discreteDict.keys())
    val = list(discreteDict.values())

    am = (arithmeticMean(discreteDict, n)) ** 2
    sum = 0
    for i in range(0, len(val)):
        sum += (kys[i] ** 2) * (val[i]) - am

    return sum / n


def meanSquareDeviation(discreteDict, n):
    return math.sqrt(dispersion(discreteDict, n))


def moment(discreteDict, n, k):
    finalList = []
    discreteKeys = list(discreteDict.keys())
    finalList.append(arithmeticMean(discreteDict, n))
    finalList.append(dispersion(discreteDict, n))
    am = arithmeticMean(discreteDict, n)

    for i in range(3, k + 1):
        sum = 0
        for j in range(0, len(discreteKeys)):
            sum += (discreteKeys[j] - am) ** i
        sum = sum / n
        finalList.append(sum)

    return finalList


def assymetry(m2, m3):
    return m3 / m2 ** (2 / 3)


def ecsess(m2, m4):
    return (m4 / m2 ** 2) - 3
