projection = input()
rows = int(input())
cols = int(input())

total_seats = rows * cols
total_price = 0

if projection == 'Premiere':
    total_price = total_seats * 12.00
    print(f'{total_price:.2f} leva')
elif projection == 'Normal':
    total_price = total_seats * 7.50
    print(f'{total_price:.2f} leva')
elif projection == 'Discount':
    total_price = total_seats * 5.00
    print(f'{total_price:.2f} leva')


