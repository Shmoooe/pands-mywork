# This program puts 10 random numbers into a list named queue.
# It then outputs all the values in the queue,
# then prints each number one at a time and shows the current numbers still in the queue.
# Author: Joanna K


import random

queue = []

for n in range(0,10):
    queue.append(random.randint(0,100))
    print(f"Queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print(f"Current number is {currentNumber} and the queue is {queue}")

print("The queue is now empty")

