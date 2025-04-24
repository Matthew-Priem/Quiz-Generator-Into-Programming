import random

my_file = open('QuizInts.txt', 'w')

for i in range(0,100):
    num = random.randint(50,200)
    my_file.write(f'{num}\n')

my_file.close()