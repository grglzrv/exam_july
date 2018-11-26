name = input()
grade = None
grades = 1
sum = 0
count =1
while grades <= 12:
    grade = float(input())
    grades += 1

    if grade < 4 or count >= 2:
        count += 1
        print(f"{name} has been excluded at {grades - 1} grade")
        break
    else:
        sum += grade

if grades >= 4 and count < 2:
    print(f"{name} graduated. Average grade: {(sum / 12):.2f}")
