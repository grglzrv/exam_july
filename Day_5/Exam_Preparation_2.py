poor_grades_count = int(input())

grades_total = 0
number_of_problems = 0
bad_number_of_problems = 0

last_problem = None
problem_name = None
grade = None

while bad_number_of_problems != poor_grades_count:
    problem_name = input()
    if problem_name == 'Enough':
        break
    grade = int(input())
    if grade <= 4:
        bad_number_of_problems += 1

    grades_total += grade
    last_problem = problem_name
    number_of_problems += 1


if bad_number_of_problems == poor_grades_count:
    print(f'You need a break, {bad_number_of_problems} poor grades.')
else:
    result = grades_total / number_of_problems
    print(f'Average score: {result:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem}')

