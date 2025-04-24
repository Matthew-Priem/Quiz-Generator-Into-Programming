num = int(input('Enter a number: '))

for possible_factor in range(1,num+1):
	if num % possible_factor == 0:
		print(possible_factor, end=' ')