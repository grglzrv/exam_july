budget = float(input())
city = input().lower()
nights = int(input())

price = 0
discount = 0
total_nights = 0

if city == 'cairo':
    price = 600 + (250 * 2) * nights
elif city == 'paris':
    price = 350 + (150 * 2) * nights
elif city == 'lima':
    price = 850 + (400 * 2) * nights
elif city == 'new york':
    price = 650 + (300 * 2) * nights
elif city == 'tokyo':
    price = 700 + (350 * 2) * nights

if (nights >= 1) and (nights <= 4):
    if city == 'cairo' or city == 'new york':
        discount = price * 3 / 100
elif (nights >= 5) and (nights <= 9):
    if city == 'cairo' or city == 'new york':
        discount = price * 5 / 100
    elif city == 'paris':
        discount = price * 7 / 100
elif (nights >= 10) and (nights <= 24):
    if city == 'cairo':
        discount = price * 10 / 100
    elif city == 'paris' or city == 'new york' or city == 'tokyo':
        discount = price * 12 / 100
elif (nights >= 25) and (nights <= 49):
    if city == 'cairo' or city == 'tokyo':
        discount = price * 17 / 100
    elif city == 'new york' or city == 'lima':
        discount = price * 19 / 100
    elif city == 'paris':
        discount = price * 22 / 100
else:
    if city == 'cairo' or city == 'tokyo' or city == 'new york' or city == 'lima' or city == 'paris':
        discount = price * 30 / 100

total_nights = price - discount
result = budget - total_nights

if result >= 0:
    print(f'Yes! You have {result:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(result):.2f} leva.')
