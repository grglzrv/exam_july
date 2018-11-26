vip_ticket = 499.99
normal_ticket = 249.99
budget = float(input())
category = input().lower()
people_count_group = int(input())

result = 0
total_price = 0

if category == 'vip':
    if 1 <= people_count_group <= 4:
        result = budget - (budget * 75 / 100)
        total_price = vip_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 5 <= people_count_group <= 9:
        result = budget - (budget * 60 / 100)
        total_price = vip_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 10 <= people_count_group <= 24:
        result = budget - (budget * 50 / 100)
        total_price = vip_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 25 <= people_count_group <= 49:
        result = budget - (budget * 40 / 100)
        total_price = vip_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif people_count_group >= 50:
        result = budget - (budget * 25 / 100)
        total_price = vip_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
else:
    if 1 <= people_count_group <= 4:
        result = budget - (budget * 75 / 100)
        total_price = normal_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 5 <= people_count_group <= 9:
        result = budget - (budget * 60 / 100)
        total_price = normal_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 10 <= people_count_group <= 24:
        result = budget - (budget * 50 / 100)
        total_price = normal_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif 25 <= people_count_group <= 49:
        result = budget - (budget * 40 / 100)
        total_price = normal_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
    elif people_count_group >= 50:
        result = budget - (budget * 25 / 100)
        total_price = normal_ticket * people_count_group
        if result > total_price:
            money_left = result - total_price
            print(f'Yes! You have {money_left:.2f} leva left.')
        else:
            not_enough_money = total_price - result
            print(f'Not enough money! You need {not_enough_money:.2f} leva.')
