# I Made Manual Changes to the slope values, ran it, then wrote the
# answers into a.py to produce my final output!  Jank!
input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

count = 0
position = 0
for i in range(0,len(inputString)):
	if i % 2 == 0:
		location = inputString[i][(position) % len(inputString[i])]
		if location == '#':
			count += 1
		position += 1
print(count)