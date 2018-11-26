import math

n1 = int(input())
n2 = int(input())
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0

for i in range(n1, n2 + 1):
    x1 = math.floor(i / 10000) % 10
    x2 = math.floor(i / 1000) % 10
    x3 = math.floor(i / 100) % 10
    x4 = math.floor(i / 10) % 10
    x5 = i % 10
    leftSum = x1 + x2
    rightSum = x4 + x5
    if leftSum == rightSum:
        print(f"{i} ", end="")
    else:
        if leftSum > rightSum:
            rightSum += x3
            if leftSum == rightSum:
                print(f"{i} ", end="")
        else:
            leftSum += x3
            if leftSum == rightSum:
                print(f"{i} ", end="")
