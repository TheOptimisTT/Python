pages_in_current_book = int(input())
pages_per_hour = int(input())
time_limit = int(input())

hours_per_day = (pages_in_current_book/pages_per_hour)/time_limit
print(hours_per_day)