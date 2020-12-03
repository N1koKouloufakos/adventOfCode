input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

count = 0

for i in range(0,len(inputString)):
	policy = inputString[i].split(':')[0]
	password = inputString[i].split(':')[1]

	position_1 = policy.split('-')[0]
	position_2 = policy.split('-')[1].split(' ')[0]
	position_1 = int(position_1)
	position_2 = int(position_2)
	letter = policy.split(' ')[1]
	if ((password[position_1] == letter) or (password[position_2] == letter)) 
	and not(password[position_1] == letter and password[position_2] == letter):
		count += 1
	# if (password[position_1] == letter and password[position_2] != letter) or (password[position_2] == letter and password[position_1] != letter):
	# 	count += 1
print(count)