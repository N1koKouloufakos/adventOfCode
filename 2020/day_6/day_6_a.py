import pdb
import re

counts = []

current = set()
for line in open("in.txt"):
	line = line.rstrip()

	# Condition to find end of group
	if line == "":
		counts.append(len(current))
		current = set()
	for letter in [char for char in line]:  
		current.add(letter)

print(sum(counts))