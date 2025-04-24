num1 = int(input("Pick a number: "))
num2 = int(input("Pick another number: "))
num3 = int(input("Pick another number: "))

count  = -1

if num1 == num2 and num1 == num3:
	count = 3
elif num1 == num2 or num1 == num3 or num2 == num3:
	count = 2
else:
	count = 0

if count > 0:
	print(f'You entered the same number {count} times.')
else:
	print('each number is unique')
