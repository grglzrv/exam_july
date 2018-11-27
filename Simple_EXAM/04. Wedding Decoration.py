budged = float(input())
type_of_goods = input()
count_goods = int(input())

spend_money = 0
money_left = 0
total_spend_money = 0
count_flower = 0
count_balloons = 0
count_candles = 0
count_ribbon = 0

while not type_of_goods == 'stop':
    if type_of_goods == 'flowers':
        count_flower += count_goods
        spend_money = count_goods * 1.5
        money_left = budged - spend_money
    elif type_of_goods == 'balloons':
        count_balloons += count_goods
        spend_money = count_goods * 0.1
        money_left = budged - spend_money
    elif type_of_goods == 'candles':
        count_candles += count_goods
        spend_money = count_goods * 0.5
        money_left = budged - spend_money
    elif type_of_goods == 'ribbon':
        count_ribbon += count_goods
        spend_money = count_goods * 2
        money_left = budged - spend_money
    budged -= spend_money
    total_spend_money += spend_money
    if budged <= 0:
        print('All money is spent!')
        print(f'Purchased decoration is {count_balloons} balloons, {count_ribbon} m ribbon, {count_flower} flowers '
              f'and {count_candles} candles.')
        break
    type_of_goods = input()
    if type_of_goods == 'stop':
        print(f'Spend money: {total_spend_money:.2f}')
        print(f'Money left: {money_left:.2f}')
        print(f'Purchased decoration is {count_balloons} balloons, {count_ribbon} m ribbon, {count_flower} flowers '
              f'and {count_candles} candles.')
        break
    count_goods = int(input())
