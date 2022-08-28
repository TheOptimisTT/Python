#•	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
type_flower = input()
number_flower = int(input())
budget = float(input())

flower_price = 0.0
discount = 1
total_price = 0.0

if type_flower == "Roses":
    flower_price = 5
    if number_flower > 80:
        discount = 0.9

elif type_flower == "Dahlias":
    flower_price = 3.8
    if number_flower > 90:
        discount = 0.85

elif type_flower == "Tulips":
    flower_price = 2.8
    if number_flower > 80:
        discount = 0.85

elif type_flower == "Narcissus":
    flower_price = 3
    if number_flower < 120:
        discount = 1.15

elif type_flower == "Gladiolus":
    flower_price = 2.5
    if number_flower < 80:
        discount = 1.2


total_price = number_flower * flower_price * discount
moneyleft = budget - total_price
if total_price <= budget:
    print(f"Hey, you have a great garden with {number_flower} {type_flower} and {abs(moneyleft):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(moneyleft):.2f} leva more.")
