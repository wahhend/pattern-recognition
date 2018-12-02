import numpy as np


def read_file():
    # read csv file
    data = []
    with open('dataset.csv') as inputfile:
        cluster = 0
        for line in inputfile:
            data.append(line.strip().split(','))
            cluster += 1

    return data


def get_distances(data):
    # find distances from and to every data with euclidean distance
    distances = np.zeros([len(data), len(data)])

    # distances = [[0 for x in range(len(results))] for y in range(len(results))]

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            distance = abs((float(data[j][0]) - float(data[i][0]))) + \
                       abs((float(data[j][1]) - float(data[i][1]))) + \
                       abs((float(data[j][2]) - float(data[i][2])))
            # distance = ((float(data[j][0]) - float(data[i][0])) ** 2 +
            #             (float(data[j][1]) - float(data[i][1])) ** 2 +
            #             (float(data[j][2]) - float(data[i][2])) ** 2 +
            #             (float(data[j][3]) - float(data[i][3])) ** 2
            #            ) ** 0.5
            distances[i][j] = distance
            distances[j][i] = distance

    return distances


def minval_index(distances):
    m = np.min(distances[np.nonzero(distances)])
    # m = np.max(distances[np.nonzero(distances)])
    # m = np.amax(distances)

    for i in range(len(distances[0])):
        for j in range(len(distances[1])):
            if distances[i][j] == m:
                return [i, j]


def clustering(data):
    clusters = np.arange(len(data))
    clusters += 1
    # clusters = str(clusters)
    print("cluster")
    print(clusters)

    distances = get_distances(data)
    print(distances)

    while len(distances) > len(data) / 2:
        index_to_merge = minval_index(distances)
        print("merged", index_to_merge)

        distances = np.delete(distances, index_to_merge[0], 1)
        # print(distances)
        distances = np.delete(distances, index_to_merge[1]-1, 1)
        # print(distances)

        to_merge = list()
        to_merge.append(distances[index_to_merge[0]])
        to_merge.append(distances[index_to_merge[1]])
        # print(to_merge)

        distances = np.delete(distances, index_to_merge[0], 0)
        distances = np.delete(distances, index_to_merge[1]-1, 0)

        new_data = np.maximum(to_merge[0], to_merge[1])
        distances = np.insert(distances, 0, new_data, 0)
        new_data = np.insert(new_data, 0, 0)
        distances = np.insert(distances, 0, new_data, 1)

        a = index_to_merge[0]
        b = index_to_merge[1]

        clusters = np.delete(clusters, index_to_merge[0])
        clusters = np.delete(clusters, index_to_merge[1])
        clusters = np.insert(clusters, 0, str(a) + str(b))

        print('cluster')
        print(clusters)
        print(distances)


if __name__ == "__main__":
    data = read_file()

    # data = [
    #     [1, 1],
    #     [4, 1],
    #     [1, 2],
    #     [3, 4],
    #     [5, 4]
    # ]
    #
    # data = [
    #     [5.1, 3.5, 1.4],
    #     [4.9, 3.0, 1.4],
    #     [7.0, 3.2, 4.7],
    #     [6.4, 3.2, 4.5],
    #     [6.3, 3.3, 6.0],
    #     [5.8, 2.7, 5.1],
    # ]
    clustering(data)

    #
    # arr = np.delete(arr, 0, 1)
    # print(arr)
