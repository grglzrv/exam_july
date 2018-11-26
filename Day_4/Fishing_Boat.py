spring_rent = 3000
summer_autumn_rent = 4200
winter_rent = 2600

budget = int(input())
season = input()
fishermans_count = int(input())

discount = 0
extra_discount = 0
money = 0 

if season == 'Spring':
    if fishermans_count <= 6:
        discount = spring_rent - (spring_rent * 10 / 100)
    elif (fishermans_count >= 7) and (fishermans_count <= 11):
        discount = spring_rent - (spring_rent * 15 / 100)
    elif fishermans_count > 11:
        discount = spring_rent - (spring_rent * 25 / 100)
    if fishermans_count % 2 == 0 and season != 'Autumn':
        extra_discount = discount - (discount * 5 / 100)
        money = budget - extra_discount
        if money < 0:
            print(f'Not enough money! You need {abs(money):.2f} leva.')
        else:
            print(f'Yes! You have {money:.2f} leva left.')
    else:
        money = budget - discount
        if money < 0:
            print(f'Not enough money! You need {abs(money):.2f} leva.')
        else:
            print(f'Yes! You have {money:.2f} leva left.')
elif season == 'Autumn' or season == 'Summer':
    if fishermans_count <= 6:
        discount = summer_autumn_rent - (summer_autumn_rent * 10 / 100)
    elif (fishermans_count >= 7) and (fishermans_count <= 11):
        discount = summer_autumn_rent - (summer_autumn_rent * 15 / 100)
    elif fishermans_count > 11:
        discount = summer_autumn_rent - (summer_autumn_rent * 25 / 100)
    if fishermans_count % 2 == 0 and season != 'Autumn':
        extra_discount = discount - (discount * 5 / 100)
        money = budget - extra_discount
        if money < 0:
            print(f'Not enough money! You need {abs(money):.2f} leva.')
        else:
            print(f'Yes! You have {money:.2f} leva left.')
    else:
        money = budget - discount
        if money < 0:
            print(f'Not enough money! You need {abs(money):.2f} leva.')
        else:
            print(f'Yes! You have {money:.2f} leva left.')
elif season == 'Winter':
    if fishermans_count <= 6:
        discount = winter_rent - (winter_rent * 10 / 100)
    elif (fishermans_count >= 7) and (fishermans_count <= 11):
        discount = winter_rent - (winter_rent * 15 / 100)
    elif fishermans_count > 11:
        discount = winter_rent - (winter_rent * 25 / 100)
    if fishermans_count % 2 == 0 and season != 'Autumn':
        extra_discount = discount - (discount * 5 / 100)
        money = budget - extra_discount
        if money < 0:
            print(f'Not enough money! You need {abs(money):.2f} leva.')
        else:
            print(f'Yes! You have {money:.2f} leva left.')
    else:
        money = budget - discount
        if money < 0:
            print(f'Not enough money! You need {abs(money):.2f} leva.')
        else:
            print(f'Yes! You have {money:.2f} leva left.')