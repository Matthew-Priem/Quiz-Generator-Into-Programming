def like_or_dislike(events):
	state = "like"
	
	for event in range(events):
		if event != state:
			state = "nothing"
		else:
			state = event
	
	return state