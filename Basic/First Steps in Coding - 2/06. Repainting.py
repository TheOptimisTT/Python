cover = int(input())
paint = int(input())
water = int(input())
hours = int(input())
bags = 0.4

cover = float((cover + 2) * 1.5)
paint = float((paint * 1.1) * 14.5)
water *= 5
matherial_cost = cover + paint + water + bags
hours *= matherial_cost * 0.3

end_sum = matherial_cost + hours
print(end_sum)