import math
name = input()
budget = float(input())
count_beer = int(input())
count_chips = int(input())

beer_price = 1.20 * count_beer
chips_1 = beer_price * (45 / 100)
price_chips = math.ceil(chips_1 * count_chips)
total_sum = beer_price + price_chips

if budget >= total_sum:
    left_money = budget - total_sum
    print(f'{name} bought a snack and has {left_money:.2f} leva left.')
else:
    left_money = budget - total_sum
    print(f'{name} needs {abs(left_money):.2f} more leva!')
