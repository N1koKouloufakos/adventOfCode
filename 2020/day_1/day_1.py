input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()

result = []
past_nums = []
for i in range(0,len(inputString)):
	#Split each word into an element of the sublist
	num = int(inputString[i])
	for i in range(0,len(past_nums)):
		past_num = past_nums[i]
		for j in range(i,len(past_nums)):
			other_num = past_nums[j]
			if num + past_num + other_num == 2020:
				print(num * past_num * other_num)
				break
	past_nums.append(num)
