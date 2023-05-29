import matplotlib.pyplot as plt
import numpy as np


def conditional_means(table, tabley):
    ni_list = []
    yn = []
    means = []

    for i in range(len(table[0])):
        sum = 0
        for j in range(len(table)):
            sum += table[j][i]
        ni_list.append(sum)

    for i in range(len(table[0])):
        sum = 0
        for j in range(len(table)):
            sum += tabley[j] * table[j][i]
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
    cord_X = []
    for i in range(len(X)):
        cord_X.append((cofs[0] * pow(X[i], 2)) + cofs[1] * X[i] + cofs[2])
    plt.clf()
    plt.plot(cord_X, Y)
    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/Quadratic.png", bbox_inches='tight')


def makeGiperbol(X, cofs):
    plt.clf()

    # plt.grid(True)
    plt.yticks(Y)
    plt.xticks(X)
    plt.savefig("C:/Users/Oleh/Documents/GitHub/Stastics-rgrshn/Quadratic.png", bbox_inches='tight')


def parabolic_corelation(X, Y):
    import numpy as np

    X_matrix = np.array([[x ** 2, x, 1] for x in X])
    Y_vector = np.array(Y)

    coefficients = np.linalg.lstsq(X_matrix, Y_vector, rcond=None)[0]
    return coefficients


def giperbolic_corelation(X, Y):

    X_matrix = np.array([1 / X, np.ones_like(X)]).T
    Y_vector = np.array(Y)

    coefficients = np.linalg.lstsq(X_matrix, Y_vector, rcond=None)[0]
    return coefficients


correlation_table = [
    [18, 0, 0, 0, 0, 0, 0],
    [2, 18, 3, 0, 0, 0, 0],
    [0, 4, 25, 2, 0, 0, 0],
    [0, 0, 0, 30, 2, 5, 0],
    [0, 0, 0, 0, 16, 4, 4],
    [0, 0, 0, 0, 0, 22, 3]
]
correlation_x = [3, 4, 7, 10, 11, 14, 17]
correlation_y = [1, 2, 2.5, 3, 4, 4.5]

correlation_means = conditional_means(correlation_table, correlation_y)
print(correlation_means)

makePlot(correlation_x, correlation_means)

coeficients = parabolic_corelation(correlation_x, correlation_means)

makeParabol(correlation_x, correlation_means, coeficients)


'''while True:
    option = int(input("enter option == "))
    if option == 1:
        makePlot(correlation_x, correlation_means)
    if option == 2:
        coeficients = parabolic_corelation(correlation_x, correlation_means)
        makeParabol(correlation_x, correlation_means, coeficients)
    if option == 3:
        break
    if option == 4:
        break
    if option == 5:
        break
    if option == 0:
        break'''
