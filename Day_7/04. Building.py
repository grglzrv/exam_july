stocks = int(input())
rooms = int(input())

latter = None

for stock_position in range(stocks, 0, -1):
    for room_position in range(0, rooms):
        if stock_position % 2 == 0:
            letter = 'O'
        else:
            letter = 'A'
        if stocks == stock_position:
            letter = 'L'
        print(f'{letter}{stock_position}{room_position} ', end='')
    print()
