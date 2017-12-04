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
	for w in range(0, len(remapped[i])):
		#Splits apart word, sorts, then rejoins the word to eliminate the possibility of anagrams
		remapped[i][w] = list(remapped[i][w])
		remapped[i][w] = sorted(remapped[i][w])
		remapped[i][w] = ''.join(remapped[i][w])
	if (isValidPhrase(remapped[i])):
		counter += 1
		print(remapped[i])

print(len(remapped))
print(counter)