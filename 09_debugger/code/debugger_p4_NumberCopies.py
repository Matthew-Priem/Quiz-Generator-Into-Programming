def count_duplicates(num_1, num_2, num_3):
	count = 0
	
	if num_1 == num_2:
		count += 1
	
	if num_1 == num_3:
		count += 1
	elif num_1 == num_3:
		count = 1
	
	if count == 1:
		return "Each number is unique"
	elif count == 3:
		return "You entered the same number 3 times"
	else:
		return "You entered the same number 2 times"