
largest = -1

user_number = int(input('Enter a number: '))
while user_number >= 0:
	if user_number % 2 == 0 and user_number > largest:
		largest = user_number
	user_number = int(input('Enter a number: '))

print(f'{largest = }')