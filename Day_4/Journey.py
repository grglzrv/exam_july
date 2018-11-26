budget = float(input())
season = input()

destination = None
money_spent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        money_spent = (budget * 30 / 100)
        print(f'Somewhere in {destination}')
        print(f'Camp - {money_spent:.2f}')
    elif season == 'winter':
        money_spent = (budget * 70 / 100)
        print(f'Somewhere in {destination}')
        print(f'Hotel - {money_spent:.2f}')
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        money_spent = (budget * 40 / 100)
        print(f'Somewhere in {destination}')
        print(f'Camp - {money_spent:.2f}')
    elif season == 'winter':
        money_spent = (budget * 80 / 100)
        print(f'Somewhere in {destination}')
        print(f'Hotel - {money_spent:.2f}')
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer' or season == 'winter':
        money_spent = (budget * 90 / 100)
        print(f'Somewhere in {destination}')
        print(f'Hotel - {money_spent:.2f}')



