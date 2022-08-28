screening_type = input()
count_rows = int(input())
count_columns = int(input())


cinema_capacity = count_rows * count_columns
ticket = 0.0

if screening_type == "Premiere":
    ticket = 12
elif screening_type == "Normal":
    ticket = 7.5
elif screening_type == "Discount":
    ticket = 5

total_price = cinema_capacity * ticket

print(f"{total_price:.2f} leva")