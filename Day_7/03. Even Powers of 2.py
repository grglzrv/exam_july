import math

n = int(input())

for number in range(0, n + 1):
    if number % 2 == 0:
        power = 2**number
        truncated_num = math.trunc(power)
        print(truncated_num)
