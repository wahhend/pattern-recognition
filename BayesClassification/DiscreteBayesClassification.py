def prior(objects, selectedClass):
    className = [object.name for object in objects]
    return (className.count(selectedClass)/len(objects))

def likelihood(objects, selectedClass, selectedFeature):
    count = 0
    classCount = 0
    for object in objects:
        if object.name == selectedClass:
            if object.feature == selectedFeature:
                count = count+1
                classCount = classCount + 1
            else:
                classCount = classCount+1
    return count/classCount

def evidence(objects, selectedFeature):
    featureName = [object.feature for object in objects]
    return (featureName.count(selectedFeature) / len(objects))

def posterior(objects, selectedClass, selectedFeature):
    return likelihood(objects, selectedClass, selectedFeature) * prior(objects, selectedClass) / evidence(objects, selectedFeature)

def decision(objects, selectedFeature):
    classes = set([object.name for object in objects])
    classes = list(classes)
    results = []
    for className in classes:
        results.append(posterior(objects, className, selectedFeature))
    return classes[results.index(max(results))]


class Object:
    name = ""
    feature = ""


fishes = []
for i in range(0, 10):
    fishes.append(Object())

fishes[0].name = "Lele"
fishes[1].name = "Lele"
fishes[2].name = "Lele"
fishes[3].name = "Lele"
fishes[4].name = "Lele"
fishes[5].name = "Lele"
fishes[6].name = "Lele"
fishes[7].name = "Patin"
fishes[8].name = "Patin"
fishes[9].name = "Patin"

for i in range(0,5):
    fishes[i].feature = "Panjang"

for i in range(5,10):
    fishes[i].feature = "Pendek"

#print(prior(fishes, "Lele"))
#print(prior(fishes, "Patin"))

#print(likelihood(fishes, "Lele", "Panjang"))
#print(likelihood(fishes, "Lele", "Pendek"))
#print(likelihood(fishes, "Patin", "Panjang"))
#print(likelihood(fishes, "Patin", "Pendek"))

#print(evidence(fishes, "Panjang"))
#print(evidence(fishes, "Pendek"))

print(posterior(fishes, "Lele", "Pendek"))
print(posterior(fishes, "Patin", "Pendek"))

print(decision(fishes, "Pendek"))

