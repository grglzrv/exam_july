count_fishes = int(input())
name = input()

count = 0
profit = 0

while not count == count_fishes:
    count += 1
    fish_kg = float(input())
    sum = 0
    if count == count_fishes:
        print(f'Lyubo fulfilled the quota!')

    for i in name:
        sum += ord(i)
    if count % 3 == 0:
        profit += sum / fish_kg
    else:
        profit -= sum / fish_kg
    if count != count_fishes:
        name = input()
        if name == 'Stop':
            break

if profit > 0:
    print(f'Lyubo\'s profit from {count} fishes is {profit:.2f} leva.')
else:
    profit = abs(profit)
    print(f'Lyubo lost {profit:.2f} leva today.')
