import math
import csv
from prettytable import PrettyTable
import numpy as np
from scipy.integrate import quad
import os

if os.name == 'nt':
    reader = csv.reader(open("C:/Users/Oleh/Documents/GitHub/Statistic/Images/Ztable.csv", "r"), delimiter=",")
    Ztable = list(reader)
    reader = csv.reader(open("C:/Users/Oleh/Documents/GitHub/Statistic/Images/dfaTable.csv", "r"), delimiter=",")
    DFATable = list(reader)
if os.name == 'posix':
    reader = csv.reader(open("/Users/olegvojtovic/Desktop/Statistic/Images/Ztable.csv", "r"), delimiter=",")
    Ztable = list(reader)
    reader = csv.reader(open("/Users/olegvojtovic/Desktop/Statistic/Images/dfaTable.csv", "r"), delimiter=",")
    DFATable = list(reader)


def printMatrix(data):
    my_table = PrettyTable()
    for i in range(0, len(data)):
        my_table.add_column(str(data[i][0]), [data[i][1], data[i][2], data[i][3]])
    print(my_table)
    print('\n')


def meanInter(data):
    meanList = []
    for i in data.items():
        if type(i[0]) is int:
            meanList.append(i[0])
        if type(i[0]) is tuple:
            temp1 = i[0][0]
            temp2 = i[0][1]
            meanList.append((temp1 + temp2) / 2)

    return meanList


def arithmeticMean(data, n, mean):
    intervalMeanList = mean
    intervalValuesDict = list(data.values())

    sum_ = 0
    for i in range(0, len(intervalMeanList)):
        sum_ += intervalValuesDict[i] * intervalMeanList[i]

    return sum_ / n


def num(data):
    s = (list(data.values()))
    sum = 0
    for i in range(0, len(s)):
        sum += s[i]
    return sum


def dev(data, n, mean):
    intervalMeanList = mean
    intervalvallist = list(data.values())
    am = arithmeticMean(data, n, mean)
    sum = 0
    for i in range(0, len(intervalMeanList)):
        sum += math.pow(intervalMeanList[i] - am, 2) * intervalvallist[i]
    sum = sum / n
    return sum


def amalgamation(data):
    checkpass = 0
    l = 1
    while checkpass != l:
        l = len(data)
        checkpass = 0
        for i in range(0, l):
            if (data[i][1] < 5.0 or data[i][3] < 10.0) or (data[i][1] < 5.0 and data[i][3] < 10.0):
                if i < l - 1:
                    if isinstance(data[i][0], tuple) and isinstance(data[i + 1][0], tuple):
                        data[i + 1][0] = (data[i][0][0], data[i + 1][0][1])
                    if isinstance(data[i][0], int) and isinstance(data[i + 1][0], tuple):
                        data[i + 1][0] = (data[i][0], data[i + 1][0][1])
                    if isinstance(data[i][0], tuple) and isinstance(data[i + 1][0], int):
                        data[i + 1][0] = (data[i][0][0], data[i + 1][0])
                    if isinstance(data[i][0], int) and isinstance(data[i + 1][0], int):
                        data[i + 1][0] = (data[i][0], data[i + 1][0])

                    data[i + 1][1] = data[i][1] + data[i + 1][1]
                    data[i + 1][2] = data[i][2] + data[i + 1][2]
                    data[i + 1][3] = data[i][3] + data[i + 1][3]
                    data.pop(i)
                    break
                if i == l - 1:
                    if isinstance(data[i][0], tuple) and isinstance(data[i - 1][0], tuple):
                        data[i - 1][0] = (data[i - 1][0][0], data[i][0][1])
                    if isinstance(data[i][0], int) and isinstance(data[i - 1][0], tuple):
                        data[i - 1][0] = (data[i - 1][0], data[i][0][1])
                    if isinstance(data[i][0], tuple) and isinstance(data[i - 1][0], int):
                        data[i - 1][0] = (data[i - 1][0][0], data[i][0])
                    if isinstance(data[i][0], int) and isinstance(data[i - 1][0], int):
                        data[i - 1][0] = (data[i - 1][0], data[i][0])

                    data[i - 1][1] = data[i][1] + data[i - 1][1]
                    data[i - 1][2] = data[i][2] + data[i - 1][2]
                    data[i - 1][3] = data[i][3] + data[i - 1][3]
                    data.pop(i)
                    break

            if (data[i][1] >= 5) and (data[i][3] >= 10):
                checkpass += 1

    return data


def binomlaw(data, arf, n):
    p = arf / n
    for i in range(0, len(data)):
        c = math.comb(n, i)
        p1 = math.pow(p, i)
        p2 = (1 - p) ** (n - i)
        data[i][2] = c * p1 * p2
        data[i][3] = n * data[i][2]

    return data


def puasonlaw(data, arf, n):
    for i in range(0, len(data)):
        data[i][2] = math.exp(-arf) * (math.pow(arf, i) / math.factorial(i))
        data[i][3] = data[i][2] * n
    return data


def evenlaw(data, d, arf, n):
    # if isinstance(data[-1][0], int):
    # data[-1][0] = (data[-1][0], 'inf')
    a = arf - math.sqrt(3) * d
    b = arf + math.sqrt(3) * d

    def f(x):
        if x < a:
            return 0
        if a <= x < b:
            return (x - a) / (b - a)
        if x >= b:
            return 1

    toremove = []
    for i in range(0, len(data)):
        if isinstance(data[i][0], tuple):
            a1 = data[i][0][0]
            b1 = data[i][0][1]
            if a <= a1 < b1 <= b:
                data[i][2] = f(data[i][0][1]) - f(data[i][0][0])
            else:
                toremove.append(i)
        else:
            if a <= data[i][0] < b:
                data[i][2] = f(data[i][0])
            else:
                toremove.append(i)

    for i in range(len(toremove) - 1, -1, -1):
        index = int(toremove[i])
        data.pop(index)

    for i in range(0, len(data)):
        data[i][3] = n * data[i][2]

    return data


def explaw(data, arf, n):
    if isinstance(data[0][0], tuple):
        data[0][0] = (0, data[0][0][1])
    else:
        data[0][0] = (0, data[0][0])
    if isinstance(data[-1][0], tuple):
        data[-1][0] = (data[-1][0][0], np.inf)
    else:
        data[-1][0] = (data[-1][0], np.inf)

    lam = 1 / arf

    def f(x):
        return lam * math.exp(-lam * x)

    for i in range(0, len(data)):
        if isinstance(data[i][0], tuple):
            a = data[i][0][0]
            b = data[i][0][1]
            I = quad(f, a, b)
            data[i][2] = I[0] - I[1]
        else:
            data[i][2] = f(data[i][0])

    for i in range(0, len(data)):
        data[i][3] = n * data[i][2]

    return data


def normallaw(data, n, arf, d):
    def makeNegative(numer):
        return -numer

    def findFi(val):
        if val == 0.0:
            return 0.0000
        val = str(val)
        if len(val) == 3:
            index = val[0:3]
            for i in range(1, len(Ztable)):
                if Ztable[i][0] == index:
                    return float('0.' + Ztable[i][1])
        if len(val) > 3:
            index = val[0:3]
            jndex = val[3]
            for i in range(1, len(Ztable)):
                if Ztable[i][0] == index:
                    for j in range(1, len(Ztable[0])):
                        if Ztable[0][j] == jndex:
                            return float('0.' + Ztable[i][j])

    if isinstance(data[0][0], tuple):
        data[0][0] = ('-inf', data[0][0][1])
    else:
        data[0][0] = ('-inf', data[0][0])
    if isinstance(data[-1][0], tuple):
        data[-1][0] = (data[-1][0][0], 'inf')
    else:
        data[-1][0] = (data[-1][0], 'inf')

    def fi(arf, d, z):
        if z == '-inf':
            return -0.5
        if z == 'inf':
            return 0.5
        else:
            rez = (z - arf) / d
            return float(rez)

    for i in range(0, len(data)):
        f1 = fi(arf, d, data[i][0][1])
        f2 = fi(arf, d, data[i][0][0])
        minusf1 = False
        minusf2 = False

        if f1 < 0:
            f1 = makeNegative(f1)
            minusf1 = True
        if f2 < 0:
            f2 = makeNegative(f2)
            minusf2 = True

        if data[i][0][0] == '-inf':
            f1 = findFi(f1)
        elif data[i][0][1] == 'inf':
            f2 = findFi(f2)
        else:
            f1 = findFi(f1)
            f2 = findFi(f2)

        if minusf1:
            f1 = makeNegative(f1)
        if minusf2:
            f2 = makeNegative(f2)

        data[i][2] = f1 - f2
        data[i][3] = n * data[i][2]

    return data


def fromDtoL(dct):
    keylist = list(dct.keys())
    vallist = list(dct.values())
    lst = []
    for i in range(0, len(keylist)):
        lst.append([keylist[i], vallist[i], 0, 0])
    return lst


def xexp(data):
    sum = 0
    for i in range(0, len(data)):
        sum += math.pow((data[i][1] - data[i][3]), 2) / data[i][3]

    return sum


def xcrt(alfa, ldata, unv):
    df = ldata - unv - 1

    for i in range(1, len(DFATable)):
        if DFATable[i][0] == str(df):
            for j in range(1, len(DFATable[0])):
                if DFATable[0][j] == str(alfa):
                    return float(DFATable[i][j])


def checkfordistribution(data, alfa, unv):
    if len(data) != 0:
        xp = xexp(data)
        xc = xcrt(alfa, len(data), unv)
        if xp >= xc:
            return False
        else:
            return True
    else:
        return False


def pirson(data, distrib, alfa):
    n = num(data)
    intervalmean = meanInter(data)
    arfmean = arithmeticMean(data, n, intervalmean)
    sd = math.sqrt(dev(data, n, intervalmean))
    data = fromDtoL(data)
    if distrib == 5:
        data = normallaw(data, n, arfmean, sd)
        data = amalgamation(data)
        return checkfordistribution(data, alfa, 2)
    if distrib == 4:
        data = explaw(data, arfmean, n)
        data = amalgamation(data)
        return checkfordistribution(data, alfa, 1)
    if distrib == 3:
        data = evenlaw(data, sd, arfmean, n)
        data = amalgamation(data)
        return checkfordistribution(data, alfa, 3)
    if distrib == 2:
        data = puasonlaw(data, arfmean, n)
        data = amalgamation(data)
        return checkfordistribution(data, alfa, 1)
    if distrib == 1:
        data = binomlaw(data, arfmean, n)
        data = amalgamation(data)
        return checkfordistribution(data, alfa, 1)
