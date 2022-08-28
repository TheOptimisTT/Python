actor_name = input()
academic_points = float(input())
evaluators_numbers = int(input())

for i in range(evaluators_numbers):
    name = input()
    points_given = float(input())
    academic_points += (points_given * len(name)) / 2
    if academic_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academic_points:.1f}!")
        break

if academic_points < 1250.5:
    print(f"Sorry, {actor_name} you need {(1250.5 - academic_points):.1f} more!")