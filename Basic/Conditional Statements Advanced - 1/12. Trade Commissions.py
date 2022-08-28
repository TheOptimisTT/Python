city = input()
sells = float(input())
commission = 0.0

if city == "Sofia":
    if 0 <= sells <= 500:
        commission = 0.05
        sells *= commission
        print(f"{sells:.2f}")
    elif 500 < sells <= 1000:
        commission = 0.07
        sells *= commission
        print(f"{sells:.2f}")
    elif 1000 < sells <= 10000:
        commission = 0.08
        sells *= commission
        print(f"{sells:.2f}")
    elif sells > 10000:
        commission = 0.12
        sells *= commission
        print(f"{sells:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sells <= 500:
        commission = 0.045
        sells *= commission
        print(f"{sells:.2f}")
    elif 500 < sells <= 1000:
        commission = 0.075
        sells *= commission
        print(f"{sells:.2f}")
    elif 1000 < sells <= 10000:
        commission = 0.1
        sells *= commission
        print(f"{sells:.2f}")
    elif sells > 10000:
        commission = 0.13
        sells *= commission
        print(f"{sells:.2f}")
    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= sells <= 500:
        commission = 0.055
        sells *= commission
        print(f"{sells:.2f}")
    elif 500 < sells <= 1000:
        commission = 0.08
        sells *= commission
        print(f"{sells:.2f}")
    elif 1000 < sells <= 10000:
        commission = 0.12
        sells *= commission
        print(f"{sells:.2f}")
    elif sells > 10000:
        commission = 0.145
        sells *= commission
        print(f"{sells:.2f}")
    else:
        print("error")
else:
    print("error")



