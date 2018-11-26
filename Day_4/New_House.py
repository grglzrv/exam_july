flower_type = input()
flowers_count = int(input())
budget = int(input())

flower_price = 0
discount_price = 0
costly_price = 0

if flower_type == 'Roses':
    if flowers_count > 80:
        flower_price = flowers_count * 5
        discount_price = flower_price - flower_price * (10 / 100)
        money = budget - discount_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
    elif flowers_count <= 80:
        flower_price = flowers_count * 5
        money = budget - flower_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
elif flower_type == 'Dahlias':
    if flowers_count > 90:
        flower_price = flowers_count * 3.80
        discount_price = flower_price - flower_price * (15 / 100)
        money = budget - discount_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
    elif flowers_count <= 90:
        flower_price = flowers_count * 3.80
        money = budget - flower_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
elif flower_type == 'Tulips':
    if flowers_count > 80:
        flower_price = flowers_count * 2.80
        discount_price = flower_price - flower_price * (15 / 100)
        money = budget - discount_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
    elif flowers_count <= 80:
        flower_price = flowers_count * 2.80
        money = budget - flower_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
elif flower_type == 'Narcissus':
    if flowers_count < 120:
        flower_price = flowers_count * 3.00
        costly_price = flower_price + flower_price * (15 / 100)
        money = budget - costly_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
    elif flowers_count >= 120:
        flower_price = flowers_count * 3.0
        money = budget - flower_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
elif flower_type == 'Gladiolus':
    if flowers_count < 80:
        flower_price = flowers_count * 2.50
        costly_price = flower_price + flower_price * (20 / 100)
        money = budget - costly_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
    elif flowers_count >= 80:
        flower_price = flowers_count * 2.50
        money = budget - flower_price
        if money < 0:
            print(f'Not enough money, you need {abs(money):.2f} leva more.')
        else:
            print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')
