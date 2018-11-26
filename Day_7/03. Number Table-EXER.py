n = int(input())

current_print_num = 1

for row in range(n):
    for col in range(n):
        current_print_num = row + col + 1
        if current_print_num > n:
            current_print_num = 2*n - current_print_num
        print(f'{current_print_num} ', end='')
    print()

