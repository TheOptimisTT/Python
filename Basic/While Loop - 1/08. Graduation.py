fails_counter = 0
average_evaluation = 0
grade = 1

student_name = input()


while grade != 13:
    yearly_evaluation = float(input())
    if yearly_evaluation >= 4:
        average_evaluation += yearly_evaluation
        grade += 1
        if grade == 13:
            break
    else:
        fails_counter += 1
        if fails_counter >= 2:
            print(f"{student_name} has been excluded at {grade} grade")
            break


if grade >= 12:
    print(f"{student_name} graduated. Average grade: {(average_evaluation/12):.2f}")