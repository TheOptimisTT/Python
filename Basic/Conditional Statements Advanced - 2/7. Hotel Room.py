month = input()
number_of_nights = int(input())

studio_price = 0
apartment_price = 0

discount_studio = 1
discount_apartment = 1
#May, June, July, August, September или October;

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if number_of_nights > 14:
    discount_apartment = 0.9

if (month == "May" or month == "October") and number_of_nights > 14:
    discount_studio = 0.7
elif (month == "May" or month == "October") and number_of_nights > 7:
    discount_studio = 0.95
elif (month == "June" or month == "September") and number_of_nights > 14:
    discount_studio = 0.8


total_apartment = apartment_price * number_of_nights * discount_apartment
total_studio = studio_price * number_of_nights * discount_studio

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
