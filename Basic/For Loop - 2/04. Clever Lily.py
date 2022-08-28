age = int(input())
washing_machine = float(input())
toy_price = int(input())

saved_money = 0.0
toys_owned = 0
birthday_money = 10.0
for i in range(1,age+1):

    if i % 2 == 0:
        saved_money += birthday_money
        birthday_money += 10
        saved_money -= 1
    else:
        toys_owned += 1

saved_money += toy_price * toys_owned

if saved_money >= washing_machine:
    print(f"Yes! {saved_money - washing_machine:.2f}")
else:
    print(f"No! {abs(saved_money - washing_machine):.2f}")