chicken_count = int(input("How many chickens do you have?: "))
cow_count = int(input("How many cows do you have?: "))
pig_count = int(input("How many pigs do you have?: "))

total_legs = chicken_count * 2 + cow_count * 4 + pig_count * 4

print(f'The total amount of legs on your farm is {total_legs}.')
