n = int(input())
odd_numbers = 0
even_numbers = 0

for i in range(1, n+1):
    k = int(input())
    if i % 2 == 0:
        even_numbers += k
    else:
        odd_numbers += k

if odd_numbers == even_numbers:
    print("Yes")
    print(f"Sum = {even_numbers}")
else:
    print("No")
    print(f"Diff = {abs(even_numbers-odd_numbers)}")