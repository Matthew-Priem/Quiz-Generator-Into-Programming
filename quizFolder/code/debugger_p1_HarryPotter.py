def convert_knuts(knuts=450):
	KNUTS_PER_SICKLE = 29
	SICKLES_PER_GALLEON = 17
	KNUTS_PER_GALLEON = KNUTS_PER_SICKLE * SICKLES_PER_GALLEON
				
	galleons = knuts // KNUTS_PER_GALLEON
	remaining_knuts = knuts // KNUTS_PER_GALLEON
				
	sickles = remaining_knuts // KNUTS_PER_SICKLE
	remaining_knuts = remaining_knuts % KNUTS_PER_SICKLE
	
	output = ""
	
	if galleons >= 0:
		if galleons > 1:
			output = output + str(galleons) + " galleons"
		else:
			output = output + str(galleons) + " galleon"
	
	if sickles > 0:
		if output:
			output = output + " "
		if sickles > 1:
			output = output + str(sickles) + " sickles"
		else:
			output = output + str(sickles) + " sickle"
	
	if remaining_knuts > 0:
		if output:
			output = output + " "
		if remaining_knuts > 1:
			output = output + str(remaining_knuts) + " knuts"
		else:
			output = output + str(remaining_knuts) + " knut"
	
	return output

