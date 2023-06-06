import discrete
import interval

n = int(input('Enter len of sample = '))
a = int(input('Enter min number = '))
b = int(input('Enter max number = '))

# дискретний розподіл частот
dskrt = discrete.discreteSample(n, a, b)
discrete.makeFileCSV(dskrt, 'mainData.csv')
discrete.makePoligon(dskrt)
discrete.makeDiagram(dskrt, 'diagram.jpg')
discrete.numericalCharacteristics(dskrt, n, 'numericalCharacteristicsDESCRETE.csv')
discrete.plot_empirical_cdf(dskrt, n)


# дискретний розподіл відносних частот
relativeDiscrete = discrete.relativeFrequencies(dskrt, n)
discrete.makeFileCSV(relativeDiscrete, 'discreteRelative.csv')
discrete.makePoligon(relativeDiscrete, 'relative')
discrete.makeDiagram(relativeDiscrete, 'diagramRELATIVE.jpg')
discrete.numericalCharacteristics(relativeDiscrete, n, 'numericalCharacteristicsDESCRETE(RELATIVE).csv')

t = int(input('Enter interval = '))

intrvl = interval.intervalSample(t)
interval.makeFileCSVInterval(intrvl, 'intervalData.csv')
interval.makeBar(intrvl)
interval.numericalCharacteristics(intrvl, n, 'numericalCharacteristicsINTERVAL.csv')

relativeInterval = interval.relativeFrequencies(intrvl, n)
interval.makeFileCSVInterval(relativeInterval, 'intervalRelative.csv')
interval.makeBar(relativeInterval, 'relative')
interval.numericalCharacteristics(relativeInterval, n, 'numericalCharacteristicsINTERVAL(RELATIVE).csv')
