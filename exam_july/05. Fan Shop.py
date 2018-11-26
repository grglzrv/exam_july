budget = int(input())
n = int(input())

total_amount = 0

for item in range(0, n):
    input_item = input()
    if input_item == 'hoodie':
        total_amount += 30
    elif input_item == 'keychain':
        total_amount += 4
    elif input_item == 'T-shirt':
        total_amount += 20
    elif input_item == 'flag':
        total_amount += 15
    elif input_item == 'sticker':
        total_amount += 1

diff = abs(total_amount - budget)
if budget >= total_amount:
    print(f'You bought {n} items and left with {diff} lv.')
else:
    print(f'Not enough money, you need {diff} more lv.')
