import pdb
import re
import string

count = 0

current = set()
rules = {}

def can_contain(bag):
	if 'no other' in rules[bag]:
		return 0

	total = 0

	for quantity, subbag in rules[bag]:
		total += quantity + quantity * (1+can_contain(subbag))

	return total

for line in open("in.txt"):
	line = line.rstrip()
	bag_type = line.split('contain')[0].replace('bags', '').rstrip().lstrip()
	containable = line.split('contain')[1].split(',')
	containable = [re.sub(r'bags|bag', '', bag) for bag in containable]
	containable = [bag.translate(str.maketrans('', '', string.punctuation)).rstrip().lstrip() for bag in containable]
	parsed_cont = []
	for bag in containable:
		if re.match(r'[0-9]', bag):
			parsed_cont.append((int(re.match(r'[0-9]', bag).group(0)), re.sub(r'[0-9]', '', bag).lstrip()))
		else:
			parsed_cont.append('no other')
	rules[bag_type] = parsed_cont


total = can_contain('shiny gold')
		
	

print(total//2)