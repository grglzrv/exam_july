import math.pi

figure = input()

if figure == 'square':
    a = float(input())
    area_s = a * a
    print(f'{area_s:.3f}')
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area_r = a * b
    print(f'{area_r:.3f}')
elif figure == 'circle':
    r = float(input())
    area_c = r * r * math.pi
    print(f'{area_c:.3f}')
else:
    a = float(input())
    h = float(input())
    area_t = a * h / 2
    print(f'{area_t:.3f}')
