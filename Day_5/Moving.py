width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

transported_box = input()
count_transported_box = 0

while not transported_box == 'Done':
    count_transported_box += int(transported_box)
    if count_transported_box >= free_space:
        break
    transported_box = input()

diff = free_space - count_transported_box

if diff >= 0:
    print(f'{diff} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(diff)} Cubic meters more.')
