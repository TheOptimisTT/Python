travel = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toys = puzzles + dolls + bears + minions + trucks
price = float(puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2)

if total_toys >= 50:
    price *= 0.75

rent = price * 0.1
price -=rent

if price >= travel:
    print(f"Yes! {(price-travel):.2f} lv left.")
else:
    print(f"Not enough money! {(travel-price):.2f} lv needed.")