n = int(input())

for i in range(0, n+1):
    print("." * (n + i), end='')
    print("#", end='')
    if i >= n/2:
        print("." * ((3*n) - 2 - (2*i)), end='')
    else:
        print("#" * ((3*n) - 2 - (2*i)), end='')
    print("#", end='')
    print("." * (n + i))

print("." * (2*n), end='')
print("#" * n, end='')
print("." * (2*n))

for m in range(0, n+2):

    if m == n//2:
        print("." * ((5*n - 10)//2), end='')
        print("D^A^N^C^E^",end='')
        print("." * ((5*n - 10)//2))
    else:
        print("." * ((2 * n) - 2), end='')
        print("#" * (n+4), end='')
        print("." * ((2 * n) - 2))

