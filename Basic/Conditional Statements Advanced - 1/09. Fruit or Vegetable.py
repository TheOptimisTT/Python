product = input()

is_f = (product == "banana" or product == "apple"\
        or product == "kiwi" or product == "cherry"\
        or product == "lemon" or product == "grapes")
is_v = (product == "tomato" or product == "cucumber"\
        or product == "pepper" or product == "carrot")

if is_f:
    print("fruit")
elif is_v:
    print("vegetable")
else:
    print("unknown")