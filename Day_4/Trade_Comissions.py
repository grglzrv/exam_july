city = input()
sale = float(input())

result = 0

if city == 'Sofia':
    if 0 <= sale <= 500:
        result = sale * 5 / 100
        print(f'{result:.2f}')
    elif 500 < sale <= 1000:
        result = sale * 7 / 100
        print(f'{result:.2f}')
    elif 1000 < sale <= 10000:
        result = sale * 8 / 100
        print(f'{result:.2f}')
    elif sale > 10000:
        result = sale * 12 / 100
        print(f'{result:.2f}')
    else:
        print('error')
elif city == 'Varna':
    if 0 <= sale <= 500:
        result = sale * 4.5 / 100
        print(f'{result:.2f}')
    elif 500 < sale <= 1000:
        result = sale * 7.5 / 100
        print(f'{result:.2f}')
    elif 1000 < sale <= 10000:
        result = sale * 10 / 100
        print(f'{result:.2f}')
    elif sale > 10000:
        result = sale * 13 / 100
        print(f'{result:.2f}')
    else:
        print('error')
elif city == 'Plovdiv':
    if 0 <= sale <= 500:
        result = sale * 5.5 / 100
        print(f'{result:.2f}')
    elif 500 < sale <= 1000:
        result = sale * 8 / 100
        print(f'{result:.2f}')
    elif 1000 < sale <= 10000:
        result = sale * 12 / 100
        print(f'{result:.2f}')
    elif sale > 10000:
        result = sale * 14.5 / 100
        print(f'{result:.2f}')
    else:
        print('error')
else:
    print('error')