highway_number = int(input('Pick a highway number: '))

if highway_number % 100 == 0:
	print('Invalid highway number')
else:
	if highway_number % 2 == 0:
		print(f'highway {highway_number} runs east/west')
	else:
		print(f'highway {highway_number} runs north/south')
