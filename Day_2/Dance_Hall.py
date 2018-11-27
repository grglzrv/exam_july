L = float(input())
W = float(input())
A = float(input())

size_hall = (L * 100) * (W * 100)
size_wardrobe = (A * 100) * (A * 100)
size_seat = size_hall / 10
free_place = (size_hall - size_wardrobe) - size_seat
count_dancers = free_place / (40 + 7000)
print(int(count_dancers))
