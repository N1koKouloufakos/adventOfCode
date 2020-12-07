input = open('in.txt', 'r')
inputString = [int(x) for x in input.read().split()]

freq = 0
pastFreqs = []
for num in inputString:
	freq += num
	if freq in pastFreqs:
		print freq
	pastFreqs.append(freq)
