cake_width = int(input())
cake_length = int(input())

pieces_taken = 0
pieces = input()

total_cake = cake_width * cake_length

while not pieces == 'STOP':
    pieces_taken = int(pieces)
    total_cake -= pieces_taken

    if total_cake < 0:
        print(f'No more cake left! You need {abs(total_cake)} pieces more.')
        break
    pieces = input()

    if pieces == 'STOP':
        print(f'{total_cake} pieces are left.')
