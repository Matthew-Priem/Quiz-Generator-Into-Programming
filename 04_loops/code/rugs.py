width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
pattern = input('Enter a pattern: ')

print('\nYour rug is:')
for i in range(length):
	for j in range(width):
		print(pattern, end="")
	print()
