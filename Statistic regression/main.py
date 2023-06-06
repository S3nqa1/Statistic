import matplotlib.pyplot as plt
import numpy as np


def ni(table):
    ni_list = []
    for i in range(len(table[0])):
        sum = 0
        for j in range(len(table)):
            sum += table[j][i]
        ni_list.append(sum)
    return ni_list


def conditional_means(table, Y, ni_list):
    yn = []
    means = []
    for i in range(len(table[0])):
        sum = 0
        for j in range(len(table)):
            sum += Y[j] * table[j][i]
        yn.append(sum)

    for i in range(len(ni_list)):
        means.append(float("{:.2f}".format(yn[i] / ni_list[i])))
    return means


def makePlot(X, Y):
    plt.clf()
    plt.plot(X, Y, marker='o', color='r', ls='')
    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/Corelation_field.png", bbox_inches='tight')


def makeParabol(X, Y, cofs):
    cord_Y = []
    for i in range(len(X)):
        cord_Y.append((cofs[0] * pow(X[i], 2)) + cofs[1] * X[i] + cofs[2])
    plt.clf()
    plt.plot(X, Y, marker='o', color='r', ls='')
    plt.plot(X, cord_Y)
    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/Quadratic.png", bbox_inches='tight')


def makeHyperbol(X, Y, cofs):
    cord_Y = []
    for i in range(len(X)):
        cord_Y.append((cofs[0] / X[i]) + cofs[1])

    plt.clf()
    plt.plot(X, Y, marker='o', color='r', ls='')
    plt.plot(X, cord_Y)
    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/Hyperbolic.png", bbox_inches='tight')


def makePower(X, Y, cofs):
    cord_Y = []
    for i in range(len(X)):
        cord_Y.append((cofs[1] * pow(cofs[0], X[i])))

    plt.clf()
    plt.plot(X, Y, marker='o', color='r', ls='')
    plt.plot(X, cord_Y)
    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/Power.png", bbox_inches='tight')


def makeSqrt(X, Y, cofs):
    cord_Y = []
    for i in range(len(X)):
        cord_Y.append(cofs[0] * np.sqrt(X[i] + cofs[1]))

    plt.clf()
    plt.plot(X, Y, marker='o', color='r', ls='')
    plt.plot(X, cord_Y)
    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/SQRT.png", bbox_inches='tight')


def parabolic_corelation(X, meanY, ni):
    k = len(X)
    sum_n = 0
    sum_xn = 0
    sum_xxn = 0
    sum_xxxn = 0
    sum_xxxxn = 0
    sum_ny = 0
    sum_xny = 0
    sum_xxny = 0

    for i in range(k):
        sum_n += ni[i]
        sum_xn += X[i] * ni[i]
        sum_xxn += pow(X[i], 2) * ni[i]
        sum_xxxn += pow(X[i], 3) * ni[i]
        sum_xxxxn += pow(X[i], 4) * ni[i]
        sum_ny += ni[i] * meanY[i]
        sum_xny += X[i] * ni[i] * meanY[i]
        sum_xxny += pow(X[i], 2) * ni[i] * meanY[i]

    left_side = np.array([[sum_xxxxn, sum_xxxn, sum_xxn], [sum_xxxn, sum_xxn, sum_xn], [sum_xxn, sum_xn, sum_n]])
    right_side = np.array([sum_xxny, sum_xny, sum_ny])

    return np.linalg.inv(left_side).dot(right_side)


def hyperbolic_corelation(X, meanY, ni):
    k = len(X)
    sum_n = 0
    sum_xn = 0
    sum_xxn = 0
    sum_yn = 0
    sum_xyn = 0

    for i in range(k):
        sum_n += ni[i]
        sum_xn += (1 / X[i]) * ni[i]
        sum_xxn += (1 / pow(X[i], 2)) * ni[i]
        sum_yn += meanY[i] * ni[i]
        sum_xyn += (1 / X[i]) * meanY[i] * ni[i]

    left_side = np.array([[sum_xn, sum_n], [sum_xxn, sum_xn]])
    right_side = np.array([sum_yn, sum_xyn])

    return np.linalg.inv(left_side).dot(right_side)


def power_corelation(X, meanY, ni):
    k = len(X)
    sum_n = 0
    sum_xn = 0
    sum_xxn = 0
    sum_yn = 0
    sum_xyn = 0

    for i in range(k):
        sum_n += ni[i]
        sum_xn += X[i] * ni[i]
        sum_xxn += pow(X[i], 2) * ni[i]
        sum_yn += np.log10(meanY[i]) * ni[i]
        sum_xyn += np.log10(meanY[i]) * ni[i] * X[i]

    left_side = np.array([[sum_xn, sum_n], [sum_xxn, sum_xn]])
    right_side = np.array([sum_yn, sum_xyn])
    cofs = np.linalg.inv(left_side).dot(right_side)
    return [np.log10(cofs[0]), np.log10(cofs[1])]


def sqrt_corelation(X, meanY, ni):
    k = len(X)
    sum_n = 0
    sum_xn = 0
    sum_xxn = 0
    sum_yn = 0
    sum_xyn = 0

    for i in range(k):
        sum_n += ni[i]
        sum_xn += np.sqrt(X[i]) * ni[i]
        sum_xxn += X[i] * ni[i]
        sum_yn += meanY[i] * ni[i]
        sum_xyn += np.sqrt(X[i]) * meanY[i] * ni[i]

    left_side = np.array([[sum_xn, sum_n], [sum_xxn, sum_xn]])
    right_side = np.array([sum_yn, sum_xyn])

    return np.linalg.inv(left_side).dot(right_side)


def dispertion(table, Y, meanY, X, ni):
    sum = 0
    for i in range(len(Y)):
        for j in range(len(X)):
            sum += pow((Y[i] - meanY[i]), 2) * table[i][j]

    sum_n = 0
    for i in range(len(ni)):
        sum_n += ni[i]

    return sum / sum_n


def sqr_sum(table, Y, meanY, X, ni):
    def yx(i):
        sum_ = 0
        for j in range(len(Y)):
            sum_ += Y[j] * table[j][i]
        return sum_ / ni[i]

    sum_ = 0
    for i in range(len(X)):
        sum_ += pow(np.abs(yx(i) - meanY[i]), 2) * ni[i]

    return sum_


correlation_x = [3, 4, 7, 10, 11, 14, 17]
correlation_y = [1, 2, 2.5, 3, 4, 4.5]
correlation_table = [
    [18, 0, 0, 0, 0, 0, 0],
    [2, 18, 3, 0, 0, 0, 0],
    [0, 4, 25, 2, 0, 0, 0],
    [0, 0, 0, 30, 2, 5, 0],
    [0, 0, 0, 0, 16, 4, 4],
    [0, 0, 0, 0, 0, 22, 3]
]

correlation_ni = ni(correlation_table)
correlation_means = conditional_means(correlation_table, correlation_y, correlation_ni)

while True:
    print("\n1 - Поле кореляції\n2 - Параболічна кореляція\n3 - Гіперболічна кореляція\n4 - Показникова кореляція\n5 - Коренева кореляція\n6 - Дисперсія\n7 - Сума квадратних відхилень умовних середніх\n0 - Вихід\n")
    option = int(input("enter option == "))
    if option == 1:
        print("Поле кореляції")
        makePlot(correlation_x, correlation_means)
        plt.show()
    if option == 2:
        print("Параболічна кореляція")
        coeficients = parabolic_corelation(correlation_x, correlation_means, correlation_ni)
        print(coeficients)
        makeParabol(correlation_x, correlation_means, coeficients)
        plt.show()
    if option == 3:
        print("Гіперболічна кореляція")
        coeficients = hyperbolic_corelation(correlation_x, correlation_means, correlation_ni)
        print(coeficients)
        makeHyperbol(correlation_x, correlation_means, coeficients)
        plt.show()
    if option == 4:
        print("Показникова кореляція")
        coeficients = power_corelation(correlation_x, correlation_means, correlation_ni)
        print(coeficients)
        makePower(correlation_x, correlation_means, coeficients)
        plt.show()
    if option == 5:
        print("Коренева кореляція")
        coeficients = sqrt_corelation(correlation_x, correlation_means, correlation_ni)
        print(coeficients)
        makeSqrt(correlation_x, correlation_means, coeficients)
        plt.show()
    if option == 6:
        print("Дисперсія")
        print(dispertion(correlation_table, correlation_y, correlation_means, correlation_x, correlation_ni))
    if option == 7:
        print("Сума квадратних відхилень умовних середніх")
        print(sqr_sum(correlation_table, correlation_y, correlation_means, correlation_x, correlation_ni))
    if option == 0:
        break
