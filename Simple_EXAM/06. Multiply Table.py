n = int(input())

rev1 = 0
rev2 = 0
rev3 = 0

reverse_num = n % 10
rev1 = int(rev1 + reverse_num)
n = n / 10

reverse_num = int(n % 10)
rev2 = int(rev2 + reverse_num)
n = n / 10

reverse_num = int(n % 10)
rev3 = int(rev3 + reverse_num)

for num3 in range(1, rev1 + 1):
    for num2 in range(1, rev2 + 1):
        for num1 in range(1, rev3 + 1):
            print(f'{num3} * {num2} * {num1} = {num3 * num2 * num1};')
