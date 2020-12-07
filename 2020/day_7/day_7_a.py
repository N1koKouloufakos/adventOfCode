import pdb
import re
import string

count = 0

current = set()
rules = {}

def can_contain(bag, goal):
	if 'no other' in rules[bag]:
		return False

	if goal in rules[bag]:
		return True

	for subbag in rules[bag]:
		if can_contain(subbag, goal):
			return True

	return False

for line in open("in.txt"):
	line = line.rstrip()
	bag_type = line.split('contain')[0].replace('bags', '').rstrip().lstrip()
	containable = line.split('contain')[1].split(',')
	containable = [re.sub(r'[0-9]', '', bag) for bag in containable]
	containable = [re.sub(r'bags|bag', '', bag) for bag in containable]
	containable = [bag.translate(str.maketrans('', '', string.punctuation)).rstrip().lstrip() for bag in containable]
	rules[bag_type] = containable

for bag_type in rules:
	if can_contain(bag_type, 'shiny gold'):
		count += 1
	
print(rules)
print(count)