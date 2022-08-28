import sys

n = input()

max_number = -sys.maxsize
while n != "Stop":
    n = int(n)
    if n > max_number:
        max_number = n
    n = input()

print(max_number)