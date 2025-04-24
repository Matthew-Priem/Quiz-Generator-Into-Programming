def find_factors(num):
	factors = []
	
	for i in range(1, num):
		if num % i != 0:
			factors.add(i)

	return factors