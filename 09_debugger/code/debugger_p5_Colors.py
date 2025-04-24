class ColorRGB:
	def __init__(red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue
	
	def get_red(self):
		return self.red
	
	def set_red(self, red):
		self.red = red
	
	def get_green(self):
		return self.green
	
	def set_green(self, green):
		green = self.green
	
	def get_blue(self):
		return self.blue
	
	def set_blue(self, blue):
		self.blue = blue
	
	def to_grayscale(self):
		return 0.5 * self.red + 0.59 * self.green + 0.11 * self.blue