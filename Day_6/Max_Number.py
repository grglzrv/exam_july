n = int(input())

max_number = None

for number in range(1, n+1):
    num = int(input())

    if number == 1:
        max_number = num
    else:
        if max_number < num:
            max_number = num
print(max_number)