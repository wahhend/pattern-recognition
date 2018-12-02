import numpy as np
import csv
import random


class Data:
    def __init__(self, feature, clustering):
        self.feature = feature
        self.clustering = clustering


def centroid(data, c):
    temp = [datas.feature for datas in data if datas.clustering == c]

    center = np.sum(temp, axis=0) / len(temp)

    return center


def distance(data, center):
    dist = (sum((data - center)**2))**0.5
    return dist


def normalize(data):
    temp = []
    for i in range(len(data)):
        temp.append((data[i]-min(data))/(max(data) - min(data)))
    return temp

# data = []
# data.append(Data([1,1], 1))
# data.append(Data([4,1], 2))
# data.append(Data([6,1], 2))
# data.append(Data([1,2], 1))
# data.append(Data([2,3], 3))
# data.append(Data([5,3], 2))
# data.append(Data([2,5], 3))
# data.append(Data([3,5], 2))
# data.append(Data([2,6], 3))
# data.append(Data([3,8], 2))


# datas = [datas.feature for datas in data]
#
# object = [datas.clustering for datas in data]
#
# temp = []
#
# delta = 1000
# threshold = 0.8
# fold = 0

# while(delta > threshold):
#     pn = 0
#     for i in range(len(datas)):
#         temp = []
#         object = [datas.clustering for datas in data]
#         print(object)
#         for j in range(1, max(object)+1):
#             x = distance(datas[i], centroid(data, j))
#             temp.append(x)
#             print(x)
#         data[i].clustering = temp.index(min(temp)) + 1
#
#         print("min", min(temp))
#         pn += min(temp)
#
#     fnew = pn
#     delta = abs(fnew - fold)
#     print(fnew, fold, delta)
#     fold = fnew
#     print("\n")


data = []

with open('k-means.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

    for row in reader:
        data.append(Data(row[1:], random.randint(1, 3)))


for i in range(4):
    x = normalize([datas.feature[i] for datas in data])
    for j in range(len(data)):
        data[j].feature[i] = x[j]


datas = [datas.feature for datas in data]

object = [datas.clustering for datas in data]

temp = []

delta = 1000
threshold = 0.8
fold = 0

while(delta > threshold):
    pn = 0
    for i in range(len(datas)):
        temp = []
        print(object[i])
        for j in range(1, max(object)+1):
            x = distance(datas[i], centroid(data, j))
            temp.append(x)
            print(x)
        data[i].clustering = temp.index(min(temp)) + 1

        print("min", min(temp))
        pn += min(temp)

    fnew = pn
    delta = abs(fnew - fold)
    print(fnew, fold, delta)
    fold = fnew
    print("\n")


# print([list.feature for list in data])
# print([list.clustering for list in data])
