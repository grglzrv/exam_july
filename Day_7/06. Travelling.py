saved_money = 0
money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while saved_money < budget:
        money = float(input())
        saved_money += money
    print(f'Going to {destination}!')
    saved_money = 0
