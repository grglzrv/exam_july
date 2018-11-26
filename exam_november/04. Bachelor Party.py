sum_signer = int(input())
count_people_group = input()

group_sum = 0
total_sum = 0
count_people = 0

while not count_people_group == 'The restaurant is full':
    count_people_group = int(count_people_group)
    count_people += count_people_group
    if count_people_group < 5:
        group_sum = count_people_group * 100
    else:
        group_sum = count_people_group * 70
    total_sum += group_sum
    count_people_group = input()

if total_sum >= sum_signer:
    result = total_sum - sum_signer
    print(f'You have {count_people} guests and {result} leva left.')
else:
    print(f'You have {count_people} guests and {total_sum} leva income, but no singer.')
