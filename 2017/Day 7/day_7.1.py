input = open('input.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

inputString = [x for x in inputString if "->" in x]
inputString = [x.split("-> ") for x in inputString]
supported = [x[1].split(", ") for x in inputString]
base = [x[0].split(" ")[0] for x in inputString]


for i in range(0, len(supported)):
	for j in range(0, len(supported[i])):
		if (supported[i][j] in base):
			base.remove(supported[i][j])

print(base)