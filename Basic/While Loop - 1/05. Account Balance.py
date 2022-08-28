deposit = input()
total_sum = 0.0

while deposit != "NoMoreMoney":
    deposit = float(deposit)
    if deposit < 0:
        print("Invalid operation!")
        break
    elif deposit >= 0:
        print(f"Increase: {deposit:.2f}")
        total_sum += deposit
    deposit = input()
print(f"Total: {total_sum:.2f}")