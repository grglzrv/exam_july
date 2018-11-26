team = input()
souvenir = input()
count_souvenir = int(input())

total_sum = 0

if (team == 'Argentina' or team == 'Brazil' or team == 'Croatia' or team == 'Denmark') and (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):

    if team == 'Argentina':
        if souvenir == 'flags':
            total_sum = count_souvenir * 3.25
        elif souvenir == 'caps':
            total_sum = count_souvenir * 7.20
        elif souvenir == 'posters':
            total_sum = count_souvenir * 5.10
        elif souvenir == 'stickers':
            total_sum = count_souvenir * 1.25
    elif team == 'Brazil':
        if souvenir == 'flags':
            total_sum = count_souvenir * 4.20
        elif souvenir == 'caps':
            total_sum = count_souvenir * 8.50
        elif souvenir == 'posters':
            total_sum = count_souvenir * 5.35
        elif souvenir == 'stickers':
            total_sum = count_souvenir * 1.20
    elif team == 'Croatia':
        if souvenir == 'flags':
            total_sum = count_souvenir * 2.75
        elif souvenir == 'caps':
            total_sum = count_souvenir * 6.90
        elif souvenir == 'posters':
            total_sum = count_souvenir * 4.95
        elif souvenir == 'stickers':
            total_sum = count_souvenir * 1.10
    elif team == 'Denmark':
        if souvenir == 'flags':
            total_sum = count_souvenir * 3.10
        elif souvenir == 'caps':
            total_sum = count_souvenir * 6.50
        elif souvenir == 'posters':
            total_sum = count_souvenir * 4.80
        elif souvenir == 'stickers':
            total_sum = count_souvenir * 0.90
    print(f'Pepi bought {count_souvenir} {souvenir} of {team} for {total_sum:.2f} lv.')
elif not (team == 'Argentina' or team == 'Brazil' or team == 'Croatia' or team == 'Denmark'):
    print('Invalid country!')
elif not (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):
    print('Invalid stock!')

