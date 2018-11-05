class Condition:
    def __init__(self, setOfValue):
        self.classification = setOfValue[len(setOfValue)-1]
        self.features = []
        for i in range(0, len(setOfValue)-1):
            self.features.append(setOfValue[i])


class Fish:
    classification = ""
    features = []

    #kumis
    features.append("")

class lantai:
    def __init__(self, setOfValue):
        self.classification = setOfValue[len(setOfValue) - 1]
        self.features = []
        for i in range(0, len(setOfValue) - 1):
            self.features.append(setOfValue[i])


def prior(objects, selectedClass):
    className = [object.classification for object in objects]
    return className.count(selectedClass)/len(objects)

def likelihood(objects, selectedClass, values):
    count = 0
    classCount = [object.classification for object in objects].count(selectedClass)

    for object in objects:
        if object.classification == selectedClass:
            sameValue = True
            for i in range(0, len(object.features)):
                if object.features[i] != values[i]:
                    sameValue = False
                    break

            if sameValue:
                count += 1

    return count/classCount

#def evidence(objects, selectedFeature):
#    featureName = [object.feature for object in objects]
#    return (featureName.count(selectedFeature) / len(objects))


def posterior(objects, selectedClass, values):
    return likelihood(objects, selectedClass, values) * prior(objects, selectedClass)


def decision(objects, values):
    classes = set([object.classification for object in objects])
    classes = list(classes)
    results = []
    for className in classes:
        results.append(posterior(objects, className, values))
    return classes[results.index(max(results))]


fishes = []
for i in range(0, 10):
    fishes.append(Fish())

fishes[0].classification = "Lele"
fishes[1].classification = "Lele"
fishes[2].classification = "Lele"
fishes[3].classification = "Lele"
fishes[4].classification = "Lele"
fishes[5].classification = "Lele"
fishes[6].classification = "Lele"
fishes[7].classification = "Patin"
fishes[8].classification = "Patin"
fishes[9].classification = "Patin"

for i in range(0,5):
    fishes[i].features = "Panjang"

for i in range(5,10):
    fishes[i].features = "Pendek"

print(posterior(fishes, "Lele", "Pendek"))
print(posterior(fishes, "Patin", "Pendek"))

print(decision(fishes, "Pendek"))


conditions = []

conditions.append(Condition([0, 1, 0, 0]))
conditions.append(Condition([1, 1, 1, 1]))
conditions.append(Condition([0, 0, 0, 0]))
conditions.append(Condition([1, 0, 0, 1]))
conditions.append(Condition([1, 1, 0, 1]))
conditions.append(Condition([0, 0, 0, 0]))
conditions.append(Condition([1, 1, 1, 0]))
conditions.append(Condition([0, 1, 1, 1]))
conditions.append(Condition([1, 0, 0, 0]))
conditions.append(Condition([1, 1, 1, 1]))

conditions.append(Condition([1, 0, 1, 0]))
conditions.append(Condition([1, 0, 1, 1]))
conditions.append(Condition([1, 1, 0, 1]))
conditions.append(Condition([0, 1, 0, 1]))
conditions.append(Condition([0, 1, 0, 0]))
conditions.append(Condition([1, 1, 1, 1]))
conditions.append(Condition([0, 0, 0, 0]))
conditions.append(Condition([0, 0, 1, 0]))
conditions.append(Condition([1, 1, 1, 1]))
conditions.append(Condition([0, 0, 0, 1]))

conditions.append(Condition([1, 0, 0, 0]))
conditions.append(Condition([0, 0, 0, 0]))
conditions.append(Condition([1, 0, 1, 1]))
conditions.append(Condition([0, 1, 0, 1]))
conditions.append(Condition([1, 1, 1, 1]))
conditions.append(Condition([1, 0, 1, 0]))
conditions.append(Condition([0, 0, 0, 0]))
conditions.append(Condition([1, 0, 1, 0]))
conditions.append(Condition([1, 0, 0, 1]))
conditions.append(Condition([0, 0, 1, 0]))

conditions.append(Condition([1, 1, 0, 1]))
conditions.append(Condition([0, 0, 1, 0]))
conditions.append(Condition([1, 0, 1, 1]))
conditions.append(Condition([0, 1, 0, 0]))
conditions.append(Condition([0, 0, 0, 0]))
conditions.append(Condition([1, 1, 0, 1]))
conditions.append(Condition([0, 0, 1, 0]))
conditions.append(Condition([1, 0, 0, 1]))
conditions.append(Condition([0, 1, 0, 0]))
conditions.append(Condition([0, 0, 1, 1]))

print(likelihood(conditions, 1, [0, 1, 0]))
print(likelihood(conditions, 0, [0, 1, 0]))

print(posterior(conditions, 1, [0, 1, 0]))
print(posterior(conditions, 0, [0, 1, 0]))

print(decision(conditions, [0, 1, 0]))


kon = []

kon.append(lantai(["kayu bakar", "ubin", "sedang"]))
kon.append(lantai(["gas LPG", "ubin", "sedang"]))
kon.append(lantai(["gas LPG", "plester", "sedang"]))
kon.append(lantai(["gas LPG", "ubin", "kaya"]))
kon.append(lantai(["kompor listrik", "ubin", "kaya"]))
kon.append(lantai(["gas LPG", "ubin", "kaya"]))
kon.append(lantai(["gas LPG", "plester", "miskin"]))
kon.append(lantai(["kayu bakar", "tanah", "miskin"]))
kon.append(lantai(["kayu bakar", "tanah", "miskin"]))
kon.append(lantai(["gas LPG", "tanah", "miskin"]))

print(decision(kon, ["kayu bakar", "tanah"]))
