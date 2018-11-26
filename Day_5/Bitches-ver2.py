__author__ = "Georgi Lazarov"
__version__ = "1.0"
__email__ = "lazarovgogo@gmail.com"

get_salary = input('salary: ').lower()

bitches_fucked_count = 0
money = 0
spent_money = 0

while not get_salary == 'no money':
    get_salary = int(get_salary)
    bitch_name = input('bitches name: ')
    spent_money = float(input('spent money: '))
    money = get_salary - spent_money
    get_salary = money
    if money < 0:
        print(f'No enough money! {abs(money):.2f}$ needed money to fuck this bitch {bitch_name}.')
        break
    bitches_fucked_count += 1

print(f'Bitches fucked - {bitches_fucked_count} counts.')

