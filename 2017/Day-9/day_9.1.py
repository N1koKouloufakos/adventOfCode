input = open('input.txt', 'r')
inputString = input.readline()
#split input into lines

openGroup = 0
skip = False
insideTrash = 0
totalGroups = 0
score = 0
skipNext = False
garbageScore = 0

for i in inputString:
	if not skipNext:
		if i == "!":
			skipNext = True
			continue

		#Inside Trash
		if insideTrash:
			if i == ">":
				insideTrash = False
			elif i == "{":
				openGroup += 1
			else:
				garbageScore += 1
		
		#Inside a group
		else:
			if i == "<":
				insideTrash = True
			elif i == "{":
				openGroup += 1
			elif i == "}":
				score += openGroup
				openGroup -= 1
				totalGroups += 1
	else:
		skipNext = False
	



print(score)


