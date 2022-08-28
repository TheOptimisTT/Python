from math import pi

enter = input()

if enter == "square":
    side = float(input())
    print(side*side)
elif enter == "rectangle":
    side = float(input())
    height = float(input())
    print(height*side)
elif enter == "triangle":
    side = float(input())
    height = float(input())
    print(height*side/2)
elif enter == "circle":
    r = float(input())
    print(pi *r*r)