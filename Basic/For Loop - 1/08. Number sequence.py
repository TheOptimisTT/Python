import sys

max_number = -sys.maxsize
min_number = sys.maxsize

numbers_entered = int(input())
for i in range(numbers_entered):
    n = int(input())
    if max_number < n:
        max_number = n
    if min_number > n:
        min_number = n
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
