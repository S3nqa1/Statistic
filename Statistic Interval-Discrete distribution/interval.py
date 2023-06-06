import csv
import math
import matplotlib.pyplot as plt

path = '/Users/olegvojtovic/Desktop/Python/Statistics/StatLab1/interval'


def makeBar(intervalDict, mode=None):
    if mode == 'relative':
        internalDict = {}
        for key, value in intervalDict.items():
            internalDict[str(f"{round(key[0], 2)} - {round(key[1], 2)}")] = value /(key[1] - key[0])

        plt.subplots(figsize=(len(internalDict.keys()) * 2, len(internalDict.values())))
        plt.bar(internalDict.keys(), internalDict.values())
        plt.yticks(list(internalDict.values()))
        plt.grid(True)
        plt.savefig(path + 'relativeIntervalHistogram.jpg', bbox_inches='tight')
    else:
        internalDict = {}
        for key, value in intervalDict.items():
            internalDict[str(f"{round(key[0], 2)} - {round(key[1], 2)}")] = (key[1] - key[0]) / value

        plt.subplots(figsize=(len(internalDict.keys()) * 2, len(internalDict.values())))
        plt.bar(internalDict.keys(), internalDict.values())
        plt.yticks(list(internalDict.values()))
        plt.grid(True)
        plt.savefig(path + 'intervalHistogram.jpg', bbox_inches='tight')


'''def plot_empirical_cdf(discreteDict):
    
    for i in range(len(Y)):
        plt.plot([edges[i], edges[i+1]],[Y[i], Y[i]], c="blue")
    plt.show()'''


def makeFileCSVInterval(intervalDict, filename):
    with open(path + filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(intervalDict.keys())
        w.writerow(intervalDict.values())


def numericalCharacteristics(intervalDict, n, filename):
    moments = moment(intervalDict, n, k=4)
    csvDict = {
        'мода': moda(intervalDict),
        'медіана': mediana(intervalDict, n),
        'с.а.': arithmeticMean(intervalDict, n),
        'розмах': swing(intervalDict),
        'девіація': dev(intervalDict, n),
        'варіанса': variance(intervalDict, n),
        'стандарт': standart(intervalDict, n),
        'варіація': variation(intervalDict, n),
        'дисперсія': dispersion(intervalDict, n),
        'c.квд.відхилення': meanSquareDeviation(intervalDict, n),
        'm1': moments[0],
        'm2': moments[1],
        'm3': moments[2],
        'm4': moments[3],
        'асиметрія': assymetry(moments[1], moments[2]),
        'ексцес': ecsess(moments[1], moments[3])

    }
    makeFileCSVInterval(csvDict, filename)


def readCSV(filename):
    with open('/Users/olegvojtovic/Desktop/Statictic/descrete/' + filename, 'r') as data:
        dict_reader = csv.DictReader(data)
        temp = list(dict_reader)

    finalDict = temp[0]
    finalDict = {int(k): int(v) for k, v in finalDict.items()}
    return finalDict


def delta(discretekeys, t):
    return (discretekeys[-1] - discretekeys[0]) / t


def intervalSample(t):
    discreteDict = readCSV("mainData.csv")
    discretekeys = list(discreteDict.keys())
    discreteval = list(discreteDict.values())
    discreteItems = []
    interPoints = []
    for i in range(0, len(discretekeys)):
        discreteItems.append([discretekeys[i], discreteval[i]])

    d = delta(discretekeys, t)
    for i in range(0, t + 1):
        interPoints.append(discretekeys[0] + d * i)

    finalDict = {}

    while len(interPoints) != 1:
        count = 0
        for key, value in discreteDict.items():
            if len(finalDict) == 0:
                if interPoints[0] <= key <= interPoints[1]:
                    count += value
                    continue
            elif (interPoints[0] < key <= interPoints[1]) and len(finalDict) != 0:
                count += value

        interval = (interPoints[0], interPoints[1])

        finalDict[interval] = count
        interPoints.pop(0)

    return finalDict


def relativeFrequencies(intervalDict, n):
    relativeDict = {}
    for key, value in intervalDict.items():
        relativeDict[key] = value / n

    return relativeDict


def meanInter(intervalDict):
    meanList = []
    for key in intervalDict.items():
        temp1 = key[0][0]
        temp2 = key[0][1]
        meanList.append((temp1 + temp2) / 2)

    return meanList


def moda(intervalDict):
    interval = max(intervalDict, key=lambda x: intervalDict[x])
    intervalList = list(intervalDict.items())
    for i in range(0, len(intervalList)):
        if intervalList[i][0] == interval:
            if i + 1 > len(intervalList) - 1:
                lastinter = [[0, 0], 0]
            else:
                lastinter = intervalList[i + 1]

            if i - 1 < 0:
                firstlist = [[0, 0], 0]
            else:
                firstlist = intervalList[i - 1]

            intervalList = [firstlist, intervalList[i], lastinter]
            break

    temp1 = intervalList[1][1] - intervalList[0][1]
    temp2 = (intervalList[1][1] - intervalList[0][1]) + (intervalList[1][1] - intervalList[2][1])
    temp3 = interval[1] - interval[0]

    return interval[0] + (temp1 / temp2) * temp3


def mediana(intervalDict, n):
    intervalList = list(intervalDict.items())
    index = math.ceil(len(intervalList) / 2)
    midINterval = intervalList[index]
    Mm = 0
    for i in range(0, len(intervalList)):
        if i < index:
            Mm += intervalList[i][1]
        else:
            break

    return midINterval[0][0] + ((midINterval[0][1] - midINterval[0][0]) / midINterval[1]) * ((n / 2) - Mm)


def arithmeticMean(intervalDict, n):
    intervalMeanList = meanInter(intervalDict)
    intervalValuesDict = list(intervalDict.values())

    sum_ = 0
    for i in range(0, len(intervalMeanList)):
        sum_ += intervalValuesDict[i] * intervalMeanList[i]

    return sum_ / n


def swing(intervalDict):
    intervalList = list(intervalDict.keys())
    x1 = intervalList[0][0]
    xn = intervalList[-1][1]
    return xn - x1


def dev(intervalDict, n):
    intervalMeanList = meanInter(intervalDict)
    am = arithmeticMean(intervalDict, n)
    sum = 0
    for i in range(0, len(intervalMeanList)):
        sum += (intervalMeanList[i] - am) ** 2
    return sum


def variance(intervalDict, n):
    return (dev(intervalDict, n)) / (n - 1)


def standart(intervalDict, n):
    return math.sqrt(variance(intervalDict, n))


def variation(intervalDict, n):
    return (standart(intervalDict, n)) / arithmeticMean(intervalDict, n)


def dispersion(intervalDIct, n):
    kys = meanInter(intervalDIct)
    val = list(intervalDIct.values())

    am = (arithmeticMean(intervalDIct, n)) ** 2
    sum = 0
    for i in range(0, len(val)):
        sum += (kys[i] ** 2) * (val[i]) - am

    return sum / n


def meanSquareDeviation(intervalDict, n):
    return math.sqrt(dispersion(intervalDict, n))


def moment(intervalDict, n, k):
    finalList = []
    discreteKeys = meanInter(intervalDict)
    finalList.append(arithmeticMean(intervalDict, n))
    finalList.append(dispersion(intervalDict, n))
    am = arithmeticMean(intervalDict, n)

    for i in range(2, k):
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
