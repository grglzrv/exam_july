a = int(input())
b = int(input())

num1 = None

while not b == 0:
    num1 = b
    b = a % b
    a = num1
print(f'{a}')


