money = input('salary: ')

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
        coints_count = int(coints_count) - 10000
        counter_100 += 1

    while coints_count >= 5000:
        coints_count = int(coints_count) - 5000
        counter_50 += 1

    while coints_count >= 2000:
        coints_count = int(coints_count) - 2000
        counter_20 += 1

    while coints_count >= 1000:
        coints_count = int(coints_count) - 1000
        counter_10 += 1

    while coints_count >= 500:
        coints_count = int(coints_count) - 500
        counter_5 += 1

    while coints_count >= 200:
        coints_count = int(coints_count) - 200
        counter_2 += 1

    while coints_count >= 100:
        coints_count = int(coints_count) - 100
        counter_1 += 1

    while coints_count >= 50:
        coints_count = int(coints_count) - 50
        counter_0_50 += 1

    while coints_count >= 20:
        coints_count = int(coints_count) - 20
        counter_0_20 += 1

    while coints_count >= 10:
        coints_count = int(coints_count) - 10
        counter_0_10 += 1

    while coints_count >= 5:
        coints_count = int(coints_count) - 5
        counter_0_05 += 1

    while coints_count >= 2:
        coints_count = int(coints_count) - 2
        counter_0_02 += 1

    while coints_count >= 1:
        coints_count = int(coints_count) - 1
        counter_0_01 += 1

    money = input('salary: ')
print('\n[=============]')
print('    Result')
print('[=============]')
print(f'100 lv. - {counter_100} br.')
print(f'50 lv. - {counter_50} br.')
print(f'20 lv. - {counter_20} br.')
print(f'10 lv. - {counter_10} br.')
print(f'5 lv. - {counter_5} br.')
print(f'2 lv. - {counter_2} br.')
print(f'1 lv. - {counter_1} br.')
print(f'0.50 lv. - {counter_0_50} br.')
print(f'0.20 lv. - {counter_0_20} br.')
print(f'0.10 lv. - {counter_0_10} br.')
print(f'0.05 lv. - {counter_0_05} br.')
print(f'0.02 lv. - {counter_0_02} br.')
print(f'0.01 lv. - {counter_0_01} br.')

exit_key = input('\nPress Enter key to exit ...')