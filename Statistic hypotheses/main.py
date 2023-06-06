import interval
import hypotheses

interval.makeStartExerciseCSV('exercise1.csv', 1)
interval.makeStartExerciseCSV('exercise2.csv', 2)

tabl1 = interval.readCSV('exercise1.csv')
tabl2 = interval.readCSV('exercise2.csv')

interval.makeBar(tabl1, '1111.jpg')
interval.makeBar(tabl2, '2222.jpg')
interval.makePoligon(tabl1, "pol111.jpg")
interval.makePoligon(tabl2, "pol222.jpg")

a = 0.05

print(hypotheses.pirson(tabl1, 5, a), 'tab1, norm')
print(hypotheses.pirson(tabl1, 4, a), 'tab1, exp')
print(hypotheses.pirson(tabl1, 3, a), 'tab1, eve')
print(hypotheses.pirson(tabl1, 2, a), 'tab1, puason')
print(hypotheses.pirson(tabl1, 1, a), 'tab1, binom')
print(hypotheses.pirson(tabl2, 5, a), 'tab2, norm')
print(hypotheses.pirson(tabl2, 4, a), 'tab2, exp')
print(hypotheses.pirson(tabl2, 3, a), 'tab2, eve')
print(hypotheses.pirson(tabl2, 2, a), 'tab2, puason')
print(hypotheses.pirson(tabl2, 1, a), 'tab2, binom')
