import math
sushi_type = input()
r_name = input()
count_portions = int(input())
order = input()

delivery = 1
total_sum = 0

res = {'Sushi Zone': {'sashimi': 4.99, 'maki': 5.29, 'uramaki': 5.99, 'temaki': 4.29},
       'Sushi Time': {'sashimi': 5.49, 'maki': 4.69, 'uramaki': 4.49, 'temaki': 5.19},
       'Sushi Bar': {'sashimi': 5.25, 'maki': 5.55, 'uramaki': 6.25, 'temaki': 4.75},
       'Asian Pub': {'sashimi': 4.50, 'maki': 4.80, 'uramaki': 5.50, 'temaki': 5.50}
       }

if order == 'Y':
    delivery = 1.20

try:
    total_sum = math.ceil(res[r_name][sushi_type] * delivery * count_portions)
except:
    print(f'{r_name} is invalid restaurant!')
else:
    print(f'Total price: {total_sum} lv.')
