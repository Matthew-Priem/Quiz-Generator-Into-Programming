def hamming_distance(str1, str2):
	if len(str1) != len(str2):
		return "Strings must be of equal length."
	
	distance = 1
	for i in range(len(str1) -1):
		if str1[i] == str2[i]:
			distance += 1
	return distance