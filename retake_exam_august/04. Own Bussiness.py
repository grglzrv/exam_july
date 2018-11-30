w_free_space = int(input())
l_free_space = int(input())
h_free_space = int(input())
count_pc = input()

total_space = w_free_space * l_free_space * h_free_space
counter_pc = 0

while not count_pc == 'Done':

    count_pc = int(count_pc)
    counter_pc += count_pc
    left = total_space - counter_pc

    if left <= 0:
        print(f'No more free space! You need {abs(left)} Cubic meters more.')
        break
    count_pc = input()
    if count_pc == 'Done':
        print(f'{left} Cubic meters left.')
        break
