name = input()

grades = 1
sum = 0

while grades <= 12:
    grade = float(input())

    if grade >= 4:
        grades += 1
        sum += grade

if grades >= 4:
    print(f"{name} graduated. Average grade: {(sum / 12):.2f}")


