a = int(input())
b = int(input())
c = int(input())
d = int(input())

for first_number in range(a, b+1):
    for second_number in range(a, b+1):
        for third_number in range(c, d+1):
            for fourth_number in range(c, d+1):
                if (first_number + fourth_number) == (second_number + third_number):
                    if (first_number != second_number) and (third_number != fourth_number):
                        print(f'{first_number}{second_number}')
                        print(f'{third_number}{fourth_number}')
                        print()
