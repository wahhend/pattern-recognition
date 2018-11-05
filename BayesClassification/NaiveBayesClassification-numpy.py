import numpy as np

luas = np.array([9,10,15,30,16,25,9,8,10,14])
masak = np.array(["kayu bakar","gas lpg","gas lpg","gas lpg","kompor listrik",
"gas lpg","gas lpg","kayu bakar","kayu bakar", "gas lpg","kayu bakar"])
lantai = np.array(["ubin","ubin","plester","ubin","ubin",
"ubin","plester", "tanah", "tanah", "tanah"])

kategori = np.array(["sedang", "sedang", "sedang",
"kaya", "kaya", "kaya",
"miskin", "miskin", "miskin", "miskin"])

ikan = ["lele", "lele", "lele", "lele", "lele", "lele", "lele",
"patin", "patin", "patin"]

kumis = ["panjang", "panjang", "panjang", "panjang", "panjang",
"pendek", "pendek", "pendek", "pendek", "pendek",]

daging = np.array([3,2,2,4,3,5,0.5,1,2,1])
# print(daging)


def naiveBayes(array,x,bahan,ubin,daging,fishName):
    hasil = likelihoodNumerik(x,array,fishName,"luas") * likelihood(array, fishName, bahan) * likelihood(array, fishName, ubin) \
            * likelihoodNumerik(daging,array,fishName,"daging") * prior(array,fishName)/ evidence(array,x)
    return hasil


def varians(data):
    hasil = np.var(data,ddof=1)
    return hasil

def mean(data):
    hasil = np.mean(data)
    return hasil

def likelihoodNumerik(x, array, fishName, feature):
    temp = np.array([])
    for fish in array:
        if (fish.name == fishName):
            if(feature=="luas"):
                temp = np.append(temp,fish.ukuran)
            else:
                temp = np.append(temp,fish.daging)

    rerata = mean(temp)
    var = varians(temp)
    hasil = 1/np.sqrt(2*np.pi*var) * np.exp(-(pow(x-rerata,2))/2*var)

    return hasil

def posterior(feature, fishName, array):
    return (likelihood(array, fishName, feature)*prior(array, fishName))/evidence(array, feature)

def prior(array, priorData):
    name = [i.name for i in array]
    count = name.count(priorData)
    count /= len(array)
    return count

def likelihood(array, fishName, feature):
    count = 0

    for fish in array:
        if(fish.name == fishName and (fish.kumis == feature or fish.lantai == feature)):
            count += 1

    name = [i.name for i in array]
    name = name.count(fishName)

    count /= name
    return count

def evidence (array, featureData):
    name = [i.kumis for i in array]
    count = name.count(featureData)
    count /= len(array)
    return count


class Fish:
    name = ""
    kumis = ""
    ukuran = ""
    lantai = ""
    daging = ""

#coba = mean(luas[0:3])


#print(likelihood(12,luas[0:3]))
fish = [Fish()] * 10

for i in range (0,9):
    fish[i] = Fish()

fish[0].kumis = "kayu bakar"
fish[1].kumis = "gas LPG"
fish[2].kumis = "gas LPG"
fish[3].kumis = "gas LPG"
fish[4].kumis = "kompor listrik"
fish[5].kumis = "gas LPG"
fish[6].kumis = "gas LPG"
fish[7].kumis = "kayu bakar"
fish[8].kumis = "kayu bakar"
fish[9].kumis = "gas LPG"

fish[0].name = "sedang"
fish[1].name = "sedang"
fish[2].name = "sedang"
fish[3].name = "kaya"
fish[4].name = "kaya"
fish[5].name = "kaya"
fish[6].name = "miskin"
fish[7].name = "miskin"
fish[8].name = "miskin"
fish[9].name = "miskin"

fish[0].ukuran = 9
fish[1].ukuran = 10
fish[2].ukuran = 15
fish[3].ukuran = 30
fish[4].ukuran = 16
fish[5].ukuran = 25
fish[6].ukuran = 9
fish[7].ukuran = 8
fish[8].ukuran = 10
fish[9].ukuran = 14

fish[0].lantai = "ubin"
fish[1].lantai = "ubin"
fish[2].lantai = "plester"
fish[3].lantai = "ubin"
fish[4].lantai = "ubin"
fish[5].lantai = "ubin"
fish[6].lantai = "plester"
fish[7].lantai = "tanah"
fish[8].lantai = "tanah"
fish[9].lantai = "tanah"

fish[0].daging = 3
fish[1].daging = 2
fish[2].daging = 2
fish[3].daging = 4
fish[4].daging = 3
fish[5].daging = 5
fish[6].daging = 0.5
fish[7].daging = 1
fish[8].daging = 2
fish[9].daging = 1


# print(prior(fish,"sedang"))

# print(posterior("kayu bakar","miskin", fish))
# print(likelihood(fish,"miskin","plester"))

# miskin

miskinLuas = likelihoodNumerik(12,fish,"miskin","luas")
sedangLuas = likelihoodNumerik(12,fish,"sedang","luas")
kayaLuas = likelihoodNumerik(12,fish,"kaya","luas")

miskinDaging = likelihoodNumerik(2,fish,"miskin","daging")
sedangDaging = likelihoodNumerik(2,fish,"sedang","daging")
kayaDaging = likelihoodNumerik(2,fish,"kaya","daging")



# print(likelihoodNumerik(12, fish, "sedang"))
#
print(naiveBayes(fish,12,"kayu bakar","plester",2))