import math
sushi_type = input()
r_name = input()
count_portions = int(input())
order = input()

total_sum = 0
delivery = 0
final_sum = 0

if (sushi_type == 'sashimi' or sushi_type == 'maki' or sushi_type == 'uramaki' or sushi_type == 'temaki') and\
        (r_name == 'Sushi Zone' or r_name == 'Sushi Time' or r_name == 'Sushi Bar' or r_name == 'Asian Pub'):

    if sushi_type == 'sashimi':
        if r_name == 'Sushi Zone':
            total_sum = count_portions * 4.99
        elif r_name == 'Sushi Time':
            total_sum = count_portions * 5.49
        elif r_name == 'Sushi Bar':
            total_sum = count_portions * 5.25
        elif r_name == 'Asian Pub':
            total_sum = count_portions * 4.50

    elif sushi_type == 'maki':
        if r_name == 'Sushi Zone':
            total_sum = count_portions * 5.29
        elif r_name == 'Sushi Time':
            total_sum = count_portions * 4.69
        elif r_name == 'Sushi Bar':
            total_sum = count_portions * 5.55
        elif r_name == 'Asian Pub':
            total_sum = count_portions * 4.80

    elif sushi_type == 'uramaki':
        if r_name == 'Sushi Zone':
            total_sum = count_portions * 5.99
        elif r_name == 'Sushi Time':
            total_sum = count_portions * 4.49
        elif r_name == 'Sushi Bar':
            total_sum = count_portions * 6.25
        elif r_name == 'Asian Pub':
            total_sum = count_portions * 5.50

    elif sushi_type == 'temaki':
        if r_name == 'Sushi Zone':
            total_sum = count_portions * 4.29
        elif r_name == 'Sushi Time':
            total_sum = count_portions * 5.19
        elif r_name == 'Sushi Bar':
            total_sum = count_portions * 4.75
        elif r_name == 'Asian Pub':
            total_sum = count_portions * 5.50
    if order == 'Y':
        delivery = total_sum * (20 / 100)
        final_sum = total_sum + delivery
        print(f'Total price: {math.ceil(final_sum)} lv.')
    else:
        print(f'Total price: {math.ceil(total_sum)} lv.')
elif not (r_name == 'Sushi Zone' or r_name == 'Sushi Time' or r_name == 'Sushi Bar' or  r_name == 'Asian Pub'):
    print(f'{r_name} is invalid restaurant!')




