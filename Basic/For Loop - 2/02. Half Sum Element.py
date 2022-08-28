import sys

number = int(input())
total_sum = 0
max_number = -sys.maxsize

for i in range(number):
    n = int(input())
    total_sum += n
    if max_number < n:
        max_number = n

if (total_sum - max_number) == max_number:
    print("Yes")
    print(f"Sum = {total_sum - max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number + max_number - total_sum)}")