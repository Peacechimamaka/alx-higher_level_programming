#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mode_num = abs(number) % 10
if number < 0:
    mode_num = -(mode_num)
if mode_num > 5:
    print(f"Last digit of {number} is {mode_num} and is greater than 5")
elif mode_num ==0 :
    print(f"Last digit of {number} is {mode_num} and is 0")
elif mode_num < 6:
    print(f"Last digit of {number} is {mode_num} and is less than 6 and not 0")
