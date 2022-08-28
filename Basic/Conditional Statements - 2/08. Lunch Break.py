from math import ceil
name = input()
episode_duration = int(input())
break_duration = int(input())

rest_time = break_duration/8
launch_time = break_duration/4
total_time = episode_duration + rest_time+ launch_time

if total_time <= break_duration:
    print(f"You have enough time to watch {name} and left with {ceil(break_duration-total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(total_time-break_duration)} more minutes.")