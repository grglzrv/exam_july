n = int(input())

count = 0

for name_s in range(ord('B'), ord('L') + 1, 2):
    for sector in range(ord('f'), ord('a')-1, - 1):
        for entrance in range(ord('A'), ord('C')+1):
            for row in range(1, 11):
                for seat in range(10, 0, - 1):
                    count += 1

                    if count == n:
                        sum = name_s + sector + entrance + row + seat
                        print(f'Ticket combination: {chr(name_s)}{chr(sector)}{chr(entrance)}{row}{seat}')
                        print(f'Prize: {sum} lv.')

