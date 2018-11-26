import getpass
print('[+======================+]')
print('     Купюр калкулатор')
print('[+======================+]\n')
username = input('Въведете потребителско име: ')
password = getpass.getpass('Въведете вашата парола: ')

while not password == 'P@ssw0rd!':
    print('Грешна парола!')
    password = getpass.getpass('Въведете вашата парола отново: ')

print('\nВъведете заплатите на служителите!\n')
money = input('заплата: ')

counter_0_01 = 0
counter_0_02 = 0
counter_0_05 = 0
counter_0_10 = 0
counter_0_20 = 0
counter_0_50 = 0
counter_1 = 0
counter_2 = 0
counter_5 = 0
counter_10 = 0
counter_20 = 0
counter_50 = 0
counter_100 = 0


while not money == 'stop':
    coints_count = float(money) * 100
    while coints_count >= 10000:
        coints_count = round(coints_count) - 10000
        counter_100 += 1

    while coints_count >= 5000:
        coints_count = round(coints_count) - 5000
        counter_50 += 1

    while coints_count >= 2000:
        coints_count = round(coints_count) - 2000
        counter_20 += 1

    while coints_count >= 1000:
        coints_count = round(coints_count) - 1000
        counter_10 += 1

    while coints_count >= 500:
        coints_count = round(coints_count) - 500
        counter_5 += 1

    while coints_count >= 200:
        coints_count = round(coints_count) - 200
        counter_2 += 1

    while coints_count >= 100:
        coints_count = round(coints_count) - 100
        counter_1 += 1

    while coints_count >= 50:
        coints_count = round(coints_count) - 50
        counter_0_50 += 1

    while coints_count >= 20:
        coints_count = round(coints_count) - 20
        counter_0_20 += 1

    while coints_count >= 10:
        coints_count = round(coints_count) - 10
        counter_0_10 += 1

    while coints_count >= 5:
        coints_count = round(coints_count) - 5
        counter_0_05 += 1

    while coints_count >= 2:
        coints_count = round(coints_count) - 2
        counter_0_02 += 1

    while coints_count >= 1:
        coints_count = round(coints_count) - 1
        counter_0_01 += 1

    money = input('заплата: ')

sum_counter = counter_0_01 * 0.01 + counter_0_02 * 0.02 + counter_0_05 * 0.05 + counter_0_10 * 0.1 + counter_0_20 * 0.2 + counter_0_50 * 0.5 + counter_1 * 1 + counter_2 * 2 + counter_5 * 5 + counter_10 * 10 + counter_20 * 20 + counter_50 * 50 + counter_100 * 100
print(f"\nОбща въведена сума: {sum_counter:.2f}")
print(f"=================================")
if counter_100 > 0:
    print(f'100 лв. -  {counter_100} бр.')
if counter_50 > 0:
    print(f'50 лв. -   {counter_50} бр.')
if counter_20 > 0:
    print(f'20 лв. -   {counter_20} бр.')
if counter_10 > 0:
    print(f'10 лв. -   {counter_10} бр.')
if counter_5 > 0:
    print(f'5 лв. -    {counter_5} бр.')
if counter_2 > 0:
    print(f'2 лв. -    {counter_2} бр.')
if counter_1 > 0:
    print(f'1 лв. -    {counter_1} бр.')
if counter_0_50 > 0:
    print(f'0.50 ст. - {counter_0_50} бр.')
if counter_0_20 > 0:
    print(f'0.20 ст. - {counter_0_20} бр.')
if counter_0_10 > 0:
    print(f'0.10 ст. - {counter_0_10} бр.')
if counter_0_05 > 0:
    print(f'0.05 ст. - {counter_0_05} бр.')
if counter_0_02 > 0:
    print(f'0.02 ст. - {counter_0_02} бр.')
if counter_0_01 > 0:
    print(f'0.01 ст. - {counter_0_01} бр.')

print(f"\n=================================")
print(f"Обща сума на купюри: {sum_counter:.2f}")
enter_exit = input('\nНатиснете ENTER бутона, за да излезете от програмата ...')
