num1 = int(input("Pick side length 1: "))
num2 = int(input("Pick side length 2: "))
num3 = int(input("Pick side length 3: "))


if num1 == num2 and num1 == num3:
	print('equilateral triangle')
elif num1 == num2 or num1 == num3 or num2 == num3:
	print('isosceles triangle')
else:
	print('scalene triangle')

