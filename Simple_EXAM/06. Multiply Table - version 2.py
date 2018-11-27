n = input()

r1 = ''
r2 = ''
r3 = ''
rev1 = 0
rev2 = 0
rev3 = 0

number = n[::-1]

r1 = number[-3:-2]
r2 = number[-2:-1]
r3 = number[-1:]

rev1 = int(r1)
rev2 = int(r2)
rev3 = int(r3)

for num3 in range(1, rev1 + 1):
    for num2 in range(1, rev2 + 1):
        for num1 in range(1, rev3 + 1):
            print(f'{num3} * {num2} * {num1} = {num3 * num2 * num1};')
