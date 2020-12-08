import pdb
import re
import string

input = open('in.txt', 'r')
inputString = input.read()
#split input into lines
inputString = inputString.splitlines()
# accumulator = 0
run_instructions = []

def run_instruction(i, accumulator, mod_list):
	if i in run_instructions:
		# print(i)
		return False
	
	run_instructions.append(i)
	try:
		a = mod_list[i]
	except IndexError:
		pdb.set_trace()
	if re.match('nop', mod_list[i]):
		run_instruction(i+1, accumulator, mod_list)
	elif re.match('acc', mod_list[i]):
		accumulator += int(mod_list[i].split(' ')[1])
		run_instruction(i+1, accumulator, mod_list)
	else:
		run_instruction(i+int(mod_list[i].split(' ')[1]), accumulator, mod_list)

	return accumulator

for i in range(len(inputString)):
	run_instructions = []
	if re.match('nop', inputString[i]):
		mod_list = inputString.copy()
		mod_list[i] = re.sub('nop', 'jmp', mod_list[i])
		# pdb.set_trace()
		run_instruction(0,0, mod_list)
	elif re.match('jmp', inputString[i]):
		mod_list = inputString.copy()
		mod_list[i] = re.sub('jmp', 'nop', mod_list[i])
		run_instruction(0,0, mod_list)