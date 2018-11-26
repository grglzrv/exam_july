n = int(input())

current_print_number = 1
check_inside_loop = False

for rows in range(1, n+1):
    for cols in range(1, rows+1):
        if current_print_number > n:
            check_inside_loop = True
            break
        print(f'{current_print_number} ', end='')
        current_print_number += 1
    if check_inside_loop:
        break
    print()
