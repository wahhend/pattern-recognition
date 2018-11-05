import math


class Object:
    name = ""
    feature = 0


def mean(objects, selectedClass):
    numOfElement = 0
    sum = 0

    for object in objects:
        if object.name == selectedClass:
            sum  = sum + object.feature
            numOfElement = numOfElement+1
    return sum/numOfElement


def variance(objects, selectedClass):
    valuesOfFeature = []
    for object in objects:
        if object.name == selectedClass:
            valuesOfFeature.append(object.feature)

    m = sum(valuesOfFeature)/len(valuesOfFeature)

    return sum((xi - m) ** 2 for xi in valuesOfFeature) / (len(valuesOfFeature)-1)


def likelihood(objects, selectedClass, value):
    var = variance(objects, selectedClass)
    m = mean(objects, selectedClass)
    return 1 / ((2 * math.pi * var) ** 0.5) \
           * math.exp(-((value - m) ** 2 / (2 * var)))


def prior(objects, selectedClass):
    className = [object.name for object in objects]
    return (className.count(selectedClass)/len(objects))


def posterior(objects, selectedClass, value):
    return likelihood(objects, selectedClass, value) * prior(objects, selectedClass)


def decision(objects, value):
    classes = set([object.name for object in objects])
    classes = list(classes)
    results = []
    for className in classes:
        results.append(posterior(objects, className, value))
    return classes[results.index(max(results))]


creatures = []

for i in range(0, 7):
    creatures.append(Object())

for i in range(0, 4):
    creatures[i].name = "Smurf"

for i in range(4, 7):
    creatures[i].name = "Troll"

creatures[0].feature = 2.7
creatures[1].feature = 2.52
creatures[2].feature = 2.57
creatures[3].feature = 2.22
creatures[4].feature = 3.16
creatures[5].feature = 3.58
creatures[6].feature = 3.16

print(decision(creatures, 2))