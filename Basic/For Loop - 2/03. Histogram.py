k = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(k):
    n = int(input())
    if n < 200:
        p1 += 1
    elif 200 <= n <= 399:
        p2 += 1
    elif 400 <= n <= 599:
        p3 += 1
    elif 600 <= n <= 799:
        p4 += 1
    else:
        p5 += 1

print(f"{p1/k*100:.2f}%")
print(f"{p2/k*100:.2f}%")
print(f"{p3/k*100:.2f}%")
print(f"{p4/k*100:.2f}%")
print(f"{p5/k*100:.2f}%")
