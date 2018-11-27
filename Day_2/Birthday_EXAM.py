l = int(input())
w = int(input())
h = int(input())
p = float(input())

v = l*w*h
total_l = v*0.001
pp = p*0.01
real_l = total_l*(1-pp)
print(f'{real_l:.3f}')

