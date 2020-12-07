import pdb
import re

# input = open('in.txt', 'r')
# inputString = input.read()
# #split input into lines
# inputString = inputString.splitlines()
# print(inputString)
count = 0
position = 0

def is_passing_condition(input):
	return True

def seat_id(row, column):
	return row*8 + column

highest = 0
ids = []
for line in open("in.txt"):
	line = line.rstrip()

	line = line.replace('F', '0')
	line = line.replace('B', '1')
	row = line[:7]
	line = line.replace('R', '1')
	line = line.replace('L', '0')
	column = line[7:]
	row = int(row, 2)
	column = int(column, 2)

	print(row)
	print(column)

	id = seat_id(row, column)
	ids.append(id)

ids.sort()
print(ids)
print(ids[605])
for i in range(0,len(ids)):
	if ids[i] + 1 != ids[i+1]:
		print(i)

print(highest)