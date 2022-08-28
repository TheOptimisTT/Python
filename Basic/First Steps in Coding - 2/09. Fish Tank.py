length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = int(input())

volume = length_cm*0.1 * width_cm*0.1 * height_cm*0.1
filled_space = volume * 0.17

result = volume - filled_space
print(result)