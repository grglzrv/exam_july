bitches_fuck = input('name: ')
money_get = float(input('money: '))

bitches_count = 0
total_money_get = 0

while not bitches_fuck == 'DEAD':
    bitches_fuck = input('name: ')
    bitches_count += 1
    total_money_get += money_get
    if bitches_fuck == 'DEAD':
        break
    money_get = float(input('money: '))

print(f'Bitches fucked - {bitches_count} counts.')

print(f'Total money get - {total_money_get:.2f}$ .')
