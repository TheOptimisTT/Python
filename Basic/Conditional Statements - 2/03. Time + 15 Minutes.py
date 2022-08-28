from math import floor

hours = int(input())
minutes = int(input())

total_minutes = 15 + minutes + hours * 60

hours = total_minutes // 60
hours = floor(hours)
minutes = total_minutes % 60

if hours >= 24:
    hours -= 24
    if minutes < 10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")
else:
    if minutes < 10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")