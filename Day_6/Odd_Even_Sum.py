n = int(input())

odd_number_position = 0
even_number_position = 0

for position in range(1, n+1):
    num = int(input())
    if position % 2 == 0:
        even_number_position += num

    else:
        odd_number_position += num

if even_number_position == odd_number_position:
    print('Yes')
    print(f'Sum = {even_number_position}')
else:
    print('No')
    diff = even_number_position - odd_number_position
    print(f'Diff = {abs(diff)}')