sector = input()
row = int(input())
seats_odd_row = int(input())

count = 0


for sectors in range(ord('A'), ord(sector) + 1):
    for rows in range(1, row + 1):
        if rows % 2 == 1:
            for seats_odd_rows in range(1, seats_odd_row + 1):
                print(f'{chr(sectors)}{rows}{chr(seats_odd_rows + 96)}')
                count += 1
        elif rows % 2 == 0:
            for seats_odd_rows in range(1, seats_odd_row + 3):
                print(f'{chr(sectors)}{rows}{chr(seats_odd_rows + 96)}')
                count += 1
    row += 1
print(f'{count}')
