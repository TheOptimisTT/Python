n = input()
score=0

length = len(n)

#for i in range(0, length):
#    if n[i] == "a":
#   elif n[i] == "e":
#        score += 2
#    elif n[i] == "i":
#        score += 3
#    elif n[i] == "o":
#        score += 4
#    elif n[i] == "u":
#        score += 5
for i in n:
    if i == "a":
        score += 1
    elif i == "e":
        score += 2
    elif i == "i":
        score += 3
    elif i == "o":
        score += 4
    elif i == "u":
        score += 5
print(score)