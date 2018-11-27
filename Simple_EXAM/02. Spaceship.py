import math
w = float(input())
length = float(input())
h = float(input())
average_h = float(input())

volume_raketa = w * length * h
volume_room = (average_h + 0.40) * 2 * 2
free_space = math.floor(volume_raketa / volume_room)

if free_space >= 3 and (free_space <= 10):
    print(f'The spacecraft holds {free_space} astronauts.')
elif free_space < 3:
    print(f'The spacecraft is too small.')
elif free_space > 10:
    print(f'The spacecraft is too big.')