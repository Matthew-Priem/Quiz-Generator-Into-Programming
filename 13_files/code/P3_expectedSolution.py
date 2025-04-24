name_file = open('MyName.txt', 'w')
name_file.write('Matt Priem')
name_file.close()

name_file = open('MyName.txt', 'r')
for letter in name_file.read():
	print(letter)

