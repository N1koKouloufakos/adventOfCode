def isValidPhrase(phrase):
	for j in range(0, len(phrase)):
		for k in range(j+1, len(phrase)):
			if (phrase[j] == phrase[k]):
				return False

	return True

input = open('input.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

remapped = []
counter = 0

for i in range(0,len(inputString)):
	#Split each word into an element of the sublist
	remapped.append(inputString[i].split(" "))


for i in range(0, len(remapped)):
	if (isValidPhrase(remapped[i])):
		counter += 1

print(counter)