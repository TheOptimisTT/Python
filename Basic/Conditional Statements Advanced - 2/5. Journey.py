budget = float(input())
season = input()

destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
    elif season == "winter":
        budget *= 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
    elif season == "winter":
        budget *= 0.8

else:
    destination = "Europe"
    budget *= 0.9

print(f"Somewhere in {destination}")

if destination == "Europe":
    print(f"Hotel - {budget:.2f}")
elif season == "summer":
    print(f"Camp - {budget:.2f}")
elif season == "winter":
    print(f"Hotel - {budget:.2f}")
