drink = input()
city = input()
quantity = float(input())
price = 0.0

if city == "Sofia":
    if drink == "coffee":
        price = quantity * 0.5
    elif drink == "water":
        price = quantity * 0.8
    elif drink == "beer":
        price = quantity * 1.2
    elif drink == "sweets":
        price = quantity * 1.45
    elif drink == "peanuts":
        price = quantity * 1.6

elif city == "Plovdiv":
    if drink == "coffee":
        price = quantity * 0.4
    elif drink == "water":
        price = quantity * 0.7
    elif drink == "beer":
        price = quantity * 1.15
    elif drink == "sweets":
        price = quantity * 1.30
    elif drink == "peanuts":
        price = quantity * 1.5

elif city == "Varna":
    if drink == "coffee":
        price = quantity * 0.45
    elif drink == "water":
        price = quantity * 0.7
    elif drink == "beer":
        price = quantity * 1.1
    elif drink == "sweets":
        price = quantity * 1.35
    elif drink == "peanuts":
        price = quantity * 1.55

print(price)