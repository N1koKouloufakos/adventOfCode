'''
If the digit is equal to the next digit, it is added to the total
The last digit looks at the first digit, so I use modulo to get back to the start
of the list.
'''

input = open('input.txt', 'r')
inputString = input.read()

#Turns inputNum into list of it's digits
digits = [int(d) for d in inputString]

#Stores the total
total = 0

for i in range(0, len(digits)):
    if (digits[i] == digits[(i+1)%len(digits)]):
        total += digits[i]

print(total)
