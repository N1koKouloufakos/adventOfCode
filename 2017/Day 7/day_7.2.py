input = open('input.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

weights = [x for x in inputString if "->" not in x]
names = [x.split(" ")[0] for x in weights]
nums = [int(x.split(" ")[1].strip("()")) for x in weights]


inputString = [x for x in inputString if "->" in x]
inputString = [x.split("-> ") for x in inputString]
supported = [x[1].split(", ") for x in inputString]
base = [x[0].split(" ")[0] for x in inputString]
baseWeights = [int(x[0].split(" ")[1].strip("()")) for x in inputString]

print(base)

for i in range(0, len(supported)):
	for j in range(0, len(supported[i])):
		if (supported[i][j] in names):
			supported[i][j] = nums[names.index(supported[i][j])]
		elif (supported[i][j] in base):
			supported[i][j] = baseWeights[base.index(supported[i][j])]

print(supported)

print(supported[base.index('eqgvf')])
