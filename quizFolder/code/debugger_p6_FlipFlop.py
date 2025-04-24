def flip_flop(word):
	length = len(word)
	middle = length // 2

	if length // 2 == 0:
		first_half = word[middle:]
		second_half = word[middle:]
		return second_half + first_half
	else:
		first_part = word[:middle]
		middle_char = word[middle]
		last_part = word[middle+1:]
		return last_part + middle_char + first_part
