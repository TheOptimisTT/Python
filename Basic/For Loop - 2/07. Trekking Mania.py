groups_of_climbers = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for i in range(groups_of_climbers):
    members = int(input())
    total_climbers += members
    if members <= 5:
        musala += members
    elif 6 <= members <= 12:
        monblan += members
    elif 13 <= members <= 25:
        kilimanjaro += members
    elif 26 <= members <= 40:
        k2 += members
    else:
        everest += members

musala = musala / total_climbers * 100
monblan = monblan / total_climbers * 100
kilimanjaro = kilimanjaro / total_climbers * 100
k2 = k2 / total_climbers * 100
everest = everest / total_climbers * 100

print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kilimanjaro:.2f}%")
print(f"{k2:.2f}%")
print(f"{everest:.2f}%")

