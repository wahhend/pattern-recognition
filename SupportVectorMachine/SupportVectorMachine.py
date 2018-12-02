class Data:
    def __init__(self, features, classification):
        self.features = features
        self.classification = classification


def normalize(data):
    temp = []
    for i in range(len(data)):
        temp.append((data[i]-min(data))/(max(data) - min(data)))

    return temp


def generate_kernel(data):
	c = 1
	d = 2
	kernel = [[0] * len(data) for d in data]

	for i in range(len(data)):
		for j in range(len(data)):
			kernel[i][j] = (data[i].features[0] * data[j].features[0] + data[i].features[1] * data[j].features[1] + c) ** d

	return kernel


def generate_decision_kernel(data, test_data):
	c = 1
	d = 2
	kernel = [[0] for d in data]

	for i in range(len(data)):
		kernel[i] = (data[i].features[0] * test_data[0] + data[i].features[1] * test_data[1] + c) ** d
	
	return kernel


def generate_y(data):
	y = [[0] * len(data) for d in data]

	for i in range(len(data)):
		for j in range(len(data)):
			y[i][j] = data[i].classification * data[j].classification
	
	return y


def generate_d(data):
	lamda = 2
	D = [[0] * len(data) for d in data]
	kernel = generate_kernel(data)
	y = generate_y(data)
	
	for i in range (len(data)):
		for j in range (len(data)):
			D[i][j] = y[i][j] * (kernel[i][j] + lamda ** 2)

	return D


def mean(arr):
	return sum(arr) / len(arr)


def find_alpha(data):
	alpha = [0 for d in data]
	E = [0 for d in data]
	C = 2
	D = generate_d(data)
	gamma = (2 / max([max(row) for row in D])) / 2
	fold = 0
	threshold = 1e-10
	delta = 1000000000

	while(delta > threshold):
		for i in range (len(alpha)):
			E[i] = sum([alpha[j] * D[i][j] for j in range(len(data))])

			new_alpha = min(max(gamma * (1 - E[i]), -alpha[i]), (C - alpha[i]))

			alpha[i] = alpha[i] + new_alpha
		
		fnew = mean(alpha)
		delta = abs(fnew - fold)
		fold = fnew
		print(delta)

	return alpha


def decide(data, test_data):
	alpha = find_alpha(data)
	results = 0
	test_data_kernel = generate_decision_kernel(data, test_data)

	for i in range (len(data)):
		temp = alpha[i] * data[i].classification * test_data_kernel[i]
		results += temp

	return results


def print_array(arr):
	for a in arr:
		print(a)


# 60 165 normal 1
# 70 160 normal 1
# 80 165 normal 1
# 100 155 tidak -1
# 40 175 tidak -1
# 60 163 ??


data = list()

data.append(Data([60, 165], 1))
data.append(Data([70, 160], 1))
data.append(Data([80, 165], 1))
data.append(Data([100, 155], -1))
data.append(Data([40, 175], -1))

test_data = [60, 163]

# for i in range(len(data[0].features)):
#     x = normalize([datas.features[i] for datas in data])
#     for j in range(len(data)):
#         data[j].features[i] = x[j]

print_array(generate_kernel(data))
print_array(generate_y(data))
print_array(generate_d(data))
find_alpha(data)

print(decide(data, test_data))
