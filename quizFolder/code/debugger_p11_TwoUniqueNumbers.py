def return_unique(numbers):

	number_dicitonary = {}
	#load dictionary
	for number in range(len(numbers)):
		if number in number_dicitonary:
			number_dicitonary[number] = 1			
		else:
			number_dicitonary[number] += 1

	unique_numbers = []
	#find unique numbers in dictionary
	for number in number_dicitonary.values():
		if number_dicitonary[number] == 1:
			unique_numbers.append(number)

	return unique_numbers
