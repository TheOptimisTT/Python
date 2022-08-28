hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam = hour_of_exam * 60 + minute_of_exam
arrival = hour_of_arrival * 60 + minute_of_arrival

time_difference = exam - arrival #if + on time if - late

hours_difference = abs(time_difference) // 60
minutes_difference = abs(time_difference) % 60

if 0 <= time_difference <= 30:
    print("On time")
    if time_difference != 0:
        print(f"{minutes_difference} minutes before the start")

elif time_difference > 30:
    print("Early")
    if hours_difference > 0 and minutes_difference >= 10:
        print(f"{hours_difference}:{minutes_difference} hours before the start")
    elif hours_difference > 0:
        print(f"{hours_difference}:0{minutes_difference} hours before the start")
    else:
        print(f"{minutes_difference} minutes before the start")

else:
    print("Late")
    if hours_difference > 0 and minutes_difference >= 10:
        print(f"{hours_difference}:{minutes_difference} hours after the start")
    elif hours_difference > 0:
        print(f"{hours_difference}:0{minutes_difference} hours after the start")
    else:
        print(f"{minutes_difference} minutes after the start")
