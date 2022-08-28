number_of_days = int(input())
type_of_room = input()
grade = input()
nights = number_of_days - 1

total_price = 0
discount = 1
room_price = 0

if type_of_room == "room for one person":
    room_price = 18
elif type_of_room == "apartment":
    room_price = 25
    if nights < 10:
        discount = 0.7
    elif 10 <= nights <= 15:
        discount = 0.65
    elif nights > 15:
        discount = 0.5

elif type_of_room == "president apartment":
    room_price = 35
    if nights < 10:
        discount = 0.9
    elif 10 <= nights <= 15:
        discount = 0.85
    elif nights > 15:
        discount = 0.8

total_price = nights * discount * room_price
if grade == "positive":
    total_price *= 1.25
elif grade == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")