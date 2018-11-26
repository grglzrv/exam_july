n = int(input())

min_number = None

for number in range(1, n+1):
    num = int(input())

    if number == 1:
        min_number = num
    else:
        if min_number > num:
            min_number = num
print(min_number)
