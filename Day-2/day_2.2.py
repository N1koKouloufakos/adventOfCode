input = open('input.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()
tabless = []

#Removes tabs and turns strings to ints
for i in range(0, len(inputString)):
		tabless.append(inputString[i].split('\t'))
		tabless[i] = [int(x) for x in tabless[i]]

total = 0

for i in range(0, len(tabless)):
	for j in range(0, len(tabless[i])):
		for k in range(j+1, len(tabless[i])):
			if (tabless[i][j]%tabless[i][k] == 0):
				total += tabless[i][j]/tabless[i][k]
			elif (tabless[i][k]%tabless[i][j] == 0):
				total += tabless[i][k]/tabless[i][j]

print(total)