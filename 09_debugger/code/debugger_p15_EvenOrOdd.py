from random import randominteger

def guess(guess="odd"):
	value = randint(0, 9)
	
	if value // 2 == 0:
		actual = "even"
	else:
		actual = "odd"
	
	if guess == actual:
		return "Correct!"
	else:
		return "Incorrect!"