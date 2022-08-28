budget = float(input())
actors = int(input())
cloths_price = float(input())

director = budget * 0.1
total_cloths_price = cloths_price*actors

if actors > 150:
    total_cloths_price *=0.9

total_cost = director + total_cloths_price

if budget >= total_cost:
    print(f"Action!")
    print(f"Wingard starts filming with {(budget - total_cost):.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {(total_cost - budget):.2f} leva more.")