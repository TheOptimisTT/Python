budget = int(input())
season = input()
number_of_fisherman = int(input())

ship_price = 0
discount = 1
total_price = 0.0
# "Spring", "Summer", "Autumn" или "Winter";

if season == "Spring":
    ship_price = 3000

elif season == "Summer" or season == "Autumn":
    ship_price = 4200

elif season == "Winter":
    ship_price = 2600

if number_of_fisherman <= 6:
    discount = 0.9
elif 7 <= number_of_fisherman <= 11:
    discount = 0.85
elif number_of_fisherman >= 12:
    discount = 0.75

total_price = ship_price * discount

if number_of_fisherman % 2 == 0 and not season == "Autumn":
    total_price *= 0.95

money_left = budget - total_price

if budget >= total_price:
    print(f"Yes! You have {abs(money_left):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")