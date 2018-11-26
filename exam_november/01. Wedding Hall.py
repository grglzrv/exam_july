import math
l_hall = float(input())
w_hall = float(input())
bar_side = float(input())

size_hall = l_hall * w_hall
size_bar = bar_side * bar_side
size_dancing = size_hall * (19 / 100)
free_space = size_hall - (size_bar + size_dancing)
count_guest = math.ceil(free_space / 3.2)
print(count_guest)
