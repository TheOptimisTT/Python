from math import floor
record = float(input())
distance = float(input())
speed = float(input())

time = floor(distance / 15) * 12.5
time = distance * speed + time

if time < record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
elif time >= record:
    print(f"No, he failed! He was {(time - record):.2f} seconds slower.")
                                                                                                                                                                                         