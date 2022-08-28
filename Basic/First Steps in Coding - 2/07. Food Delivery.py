chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())
delivery = 2.5

chicken_menu *= 10.35
fish_menu *= 12.4
veg_menu *= 8.15

desert = (chicken_menu + fish_menu + veg_menu) * 0.2

total = chicken_menu + fish_menu + veg_menu + desert + delivery

print(total)