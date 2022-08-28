from math import floor

tournaments_number = int(input())
score_starting = int(input())

avg_points = -score_starting
win_rate = 0
for i in range(tournaments_number):
    result = input()

    if result == "W":
        score_starting+=2000
        win_rate += 1
    elif result == "F":
        score_starting+=1200
    elif result == "SF":
        score_starting+=720

avg_points += score_starting
avg_points /= tournaments_number
win_rate = win_rate/tournaments_number * 100

print(f"Final points: {score_starting}")
print(f"Average points: {floor(avg_points)}")
print(f"{win_rate:.2f}%")