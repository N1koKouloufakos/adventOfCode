input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

count = 0
position = 0
for i in range(0,len(inputString)):
	location = inputString[i][(position) % len(inputString[i])]
	if location == '#':
		count += 1
	position += 3
print(count)