import pdb
input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()
print(inputString)
count = 0
position = 0
byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False
def is_valid(passport):
	return True

previous_index = 0
for i in range(0,len(inputString)):
	byr = False
	iyr = False
	eyr = False
	hgt = False
	hcl = False
	ecl = False
	pid = False
	cid = False
	line = inputString[i]
	if line == '':

		for j in range(previous_index, i):
			if 'byr:' in inputString[j]:
				byr = True
			if 'iyr:' in inputString[j]:
				iyr = True
			if 'eyr:' in inputString[j]:
				eyr = True
			if 'hgt:' in inputString[j]:
				print('hello', j)
				print(inputString[j])
				hgt = True
			if 'hcl:' in inputString[j]:
				hcl = True
			if 'ecl:' in inputString[j]:
				ecl = True
			if 'pid:' in inputString[j]:
				pid = True
			if 'cid:' in inputString[j]:
				cid = True
		if byr and iyr and eyr and hgt and hcl and ecl and pid:
				count += 1

		previous_index = i+1
			
print(count)