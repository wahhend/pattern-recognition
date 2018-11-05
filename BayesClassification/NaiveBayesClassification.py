import math


class Data:
    def __init__(self, discreteFeature, numericFeature, classification):
        self.classification = classification
        self.discreteFeatures = discreteFeature
        self.numericFeatures = numericFeature


def prior(objects, selectedClass):
    className = [object.classification for object in objects]
    return className.count(selectedClass)/len(objects)


def likelihood(objects, selectedClass, values):
    likely = 1
    classCount = [object.classification for object in objects].count(selectedClass)

    for i in range(0, len(values)):
        count = 0
        for object in objects:
            if object.classification == selectedClass and object.discreteFeatures[i] == values[i]:
                count += 1

        likely *= (count / classCount)

    return likely


def mean(data):
    return sum(data) / len(data)


def variance(data):
    m = mean(data)
    return sum((xi - m) ** 2 for xi in data) / (len(data)-1)


def numericLikelihood(objects, selectedClass, values):
    likely = 1
    # classCount = [object.classification for object in objects].count(selectedClass)
    filteredObjects = [object for object in objects if object.classification == selectedClass]

    for i in range(0, len(values)):
        var = variance([object.numericFeatures[i] for object in filteredObjects])
        m = mean([object.numericFeatures[i] for object in filteredObjects])

        likely *= (1 / ((2 * math.pi * var) ** 0.5) * math.exp(-((values[i] - m) ** 2 / (2 * var))))

    return likely


def posterior(objects, selectedClass, discreteValues, numericValues):
    return likelihood(objects, selectedClass, discreteValues) * numericLikelihood(objects, selectedClass, numericValues) * prior(objects, selectedClass)


def decision(objects, discreterValues, numericValues):
    classes = set([object.classification for object in objects])
    classes = list(classes)
    results = []
    for className in classes:
        results.append(posterior(objects, className, discreterValues, numericValues))
    return classes[results.index(max(results))]


data = []

data.append(Data(["kayu bakar", "ubin"], [9, 3], "sedang"))
data.append(Data(["gas LPG", "ubin"], [10, 2], "sedang"))
data.append(Data(["gas LPG", "plester"], [15, 2], "sedang"))
data.append(Data(["gas LPG", "ubin"], [30, 4], "kaya"))
data.append(Data(["kompor listrik", "ubin"], [16, 3], "kaya"))
data.append(Data(["gas LPG", "ubin"], [25, 5], "kaya"))
data.append(Data(["gas LPG", "plester"], [9, 0.5], "miskin"))
data.append(Data(["kayu bakar", "tanah"], [8, 1], "miskin"))
data.append(Data(["kayu bakar", "tanah"], [10, 2], "miskin"))
data.append(Data(["gas LPG", "tanah"], [14, 1], "miskin"))

print(decision(data, ["kayu bakar", "plester"], [12, 2]))