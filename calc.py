a = float(input('First number>> '))
b = float(input('Second number>> '))
c = input('Operation>> ')


if c == '+' : 
	print(a + b)
if c == '-' : 
	print(a - b)
if c == '*' : 
	print(a * b)

try :
	if c == '/' : 
		print(a / b)
except ZeroDivisionError :
	print('Zero devision error, please try again.')
