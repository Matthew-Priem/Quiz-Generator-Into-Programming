class Recipe:
	def __init__(name, cooking_time):
		self.name = name
		self.cooking_time = cooking_time
	
	def get_name(self):
		return self.name
	
	def set_name(self, name):
		self.name = name
	
	def get_cooking_time(self):
		return cooking_time
	
	def set_cooking_time(self, cooking_time):
		self.cooking_time = cooking_time
	
	def is_quick_meal(self):
		return self.cooking_time == 30