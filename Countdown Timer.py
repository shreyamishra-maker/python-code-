 import time

num = int(input("Enter time in seconds: "))

while num > 0:
    print(num)
    time.sleep(1)
    num -= 1

print("Time's up!")
