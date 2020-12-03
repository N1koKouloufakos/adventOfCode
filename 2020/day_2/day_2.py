input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

count = 0

for i in range(0,len(inputString)):
	policy = inputString[i].split(':')[0]
	password = inputString[i].split(':')[1]

	min_num = policy.split('-')[0]
	max_num = policy.split('-')[1].split(' ')[0]
	min_num = int(min_num)
	max_num = int(max_num)
	letter = policy.split(' ')[1]

	num_letters_in_password = password.count(letter)
	if min_num <= num_letters_in_password and num_letters_in_password <= max_num:
		count += 1
print(count)