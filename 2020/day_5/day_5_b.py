import pdb
import re

input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

count = 0
position = 0

def is_valid(passport):
	byr = False
	iyr = False
	eyr = False
	hgt = False
	hcl = False
	ecl = False
	pid = False
	# print(passport)

	for entry in passport:
		code, value = entry.split(':')

		if 'byr' == code and (int(value) >= 1920 and int(value) <= 2002):
			byr = True
		if 'iyr' == code and (int(value) >= 2010 and int(value) <= 2020):
			iyr = True
		if 'eyr' == code and (int(value) >= 2020 and int(value) <= 2030):
			eyr = True
		if 'hgt' == code:
			if re.search("(1[5-8][0-9]|19[0-3])cm", value):
			 hgt = True
			elif re.search("(59|6[0-9]|7[0-6])in", value):
			 hgt = True
		if 'hcl' == code:
			if re.search("#[a-f0-9]{6}", value):
				hcl = True
		if 'ecl' == code:
			if re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", value):
				ecl = True
		if 'pid' == code:
			if re.search("[0-9]{9}", value):
				pid = True
	if byr and iyr and eyr and hgt and hcl and ecl and pid:
		print(passport)
		return True
	else:
		print(byr, iyr, eyr, hgt, hcl, ecl, pid)
		return False

previous_index = 0
parsed_input = []
counter = 0
for i in range(0,len(inputString)):
	# pdb.set_trace()
	line = inputString[i]
	if line == '':
		passport = ''
		for j in range(previous_index, i):
			passport += ' ' + inputString[j]
		previous_index = i+1
		parsed_input.append(passport.rstrip())	
print(len(parsed_input))
# print(parsed_input)
for i in range(0, len(parsed_input)):
	passport = parsed_input[i].split()
	# pdb.set_trace()
	if is_valid(passport):
		# print(passport)
		count += 1
	# There's technically enough element to potentially be valid

# THIS ANSWER DOESN"T ACTUALLY WORK, THERE"S AN EDGE CASE THAT I DIDN"T CATCH
print(count)		
# print(parsed_input)