number1 = int(input())
number2 = int(input())
operator_used = input()
result = 0

# •	Ако операцията е събиране, изваждане или умножение:
# o	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
if operator_used == "+" or operator_used == "-" or operator_used == "*":
    if operator_used == "+":
        result = number2 + number1
    elif operator_used == "-":
        result = number1 - number2
    else:
        result = number2 * number1
    if abs(result) % 2 == 0:
        print(f"{number1} {operator_used} {number2} = {result} - even")
    else:
        print(f"{number1} {operator_used} {number2} = {result} - odd")

elif number2 == 0:
    print(f"Cannot divide {number1} by zero")

elif operator_used == "/":
    result = number1 / number2
    print(f"{number1} {operator_used} {number2} = {result:.2f}")

elif operator_used == "%":
    result = number1 % number2
    print(f"{number1} {operator_used} {number2} = {result}")
