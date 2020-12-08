import pdb
import re
import string

input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()
# accumulator = 0
run_instructions = []

def run_instruction(i, accumulator):
	if i in run_instructions:
		print(accumulator)
		return
	
	run_instructions.append(i)
	if re.match('nop', inputString[i]):
		run_instruction(i+1, accumulator)
	elif re.match('acc', inputString[i]):
		accumulator += int(inputString[i].split(' ')[1])
		run_instruction(i+1, accumulator)
	else:
		run_instruction(i+int(inputString[i].split(' ')[1]), accumulator)

run_instruction(0, 0)
