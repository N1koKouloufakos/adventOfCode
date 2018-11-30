'''
If the digit is equal to the digit half the length of the list away,
then it is added to the total.  
'''

input = open('input.txt', 'r')
inputString = input.read()

#Turns inputNum into list of it's digits
digits = [int(d) for d in inputString]

#Stores the total
total = 0

for i in range(0, len(digits)):
    if (digits[i] == digits[(i+int(len(digits)/2))%len(digits)]):
        total += digits[i]

print(total)
