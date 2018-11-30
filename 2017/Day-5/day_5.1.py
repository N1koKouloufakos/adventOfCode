input = open('input.txt', 'r')
inputString = [int(x) for x in input.read().split()]

print(inputString)
nextIndex = 0
index = 0
steps = 0

while (nextIndex < len(inputString) and nextIndex >= 0):
	nextIndex += inputString[index]
	inputString[index] += 1
	index = nextIndex
	steps += 1

print(steps)