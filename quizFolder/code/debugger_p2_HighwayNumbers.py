def highway_directions(highway_num):
	if 1 < highway_num < 99:
		if highway_num % 2 == 0:
			return f"I-{highway_num} runs east/west"
		else:
			return f"I-{highway_num} runs north/south"

	elif 100 > highway_num > 999:
		service_highway = highway_num % 100

		if 1 <= service_highway <= 99:
			if service_highway % 2 == 0:
				return f"I-{highway_num} runs east/west"
			elif:
				return f"I-{highway_num} runs north/south"
		else:
			return f"I-{highway_num} is an invalid highway number"
	else:
		return f"I-{highway_num} is an invalid highway number"