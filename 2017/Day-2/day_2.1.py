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
		largest = max(tabless[i])
		smallest = min(tabless[i])
		total += largest-smallest

print total