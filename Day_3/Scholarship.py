import math

salary = float(input())
average_success = float(input())
minimal_salary = float(input())

get_social_scholarship: float = 0
get_excellent_scholarship: float = 0

get_social_scholarship = math.floor(minimal_salary * 35 / 100)
get_excellent_scholarship = math.floor(average_success * 25)


if salary > minimal_salary and average_success < 4.5:
    print('You cannot get a scholarship!')
elif salary < minimal_salary and average_success >= 5.5 and get_excellent_scholarship > get_social_scholarship:
    print(f'You get a scholarship for excellent results {get_excellent_scholarship} BGN')
elif salary < minimal_salary and average_success > 4.5:
    print(f'You get a Social scholarship {get_social_scholarship} BGN')
elif salary < minimal_salary and average_success >= 5.5 and get_excellent_scholarship < get_social_scholarship:
    print(f'You get a Social scholarship {get_social_scholarship} BGN')
elif salary >= minimal_salary and average_success >= 5.5:
    print(f'You get a scholarship for excellent results {get_excellent_scholarship} BGN')
else:
    print('You cannot get a scholarship!')
