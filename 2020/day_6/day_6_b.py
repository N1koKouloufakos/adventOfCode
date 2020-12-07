import pdb
import re

counts = []

current = set()
first = True
for line in open("in.txt"):
	line = line.rstrip()

	# Condition to find end of group
	if line == "":
		counts.append(len(current))
		current = set()
		first = True
		continue

	if first == True:
		for letter in [char for char in line]:  
			current.add(letter)
		first = False
	else:
		line_set = set([char for char in line])
		current = current.intersection(line_set)  
				

print(sum(counts))