n = int(input())
name = input()

all_grade_sum = 0
all_grade_count = 0

while not name == 'Finish':
    current_grade_sum = 0
    for i in range(1, n + 1):
        all_grade_count += 1
        current_grade = float(input())
        current_grade_sum += current_grade
        all_grade_sum +=  current_grade
    current_average = current_grade_sum / n
    print(f'{name} - {current_average:.2f}.')
    name = input()
all_average = all_grade_sum / all_grade_count
print(f'Student\'s final assessment is {all_average:.2f}.')
