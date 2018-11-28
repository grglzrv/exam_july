n = int(input())

for i in range(0, n):
    print("%s~ ~ ~" % (' ' * n))

print('=' * (3*n+5))

for m in range(1, n-1):
    if m == (n//2):
        print("|", end='')
        print("%s" % ('~' * n), end='')
        print("JAVA", end='')
        print("%s" % ('~' * n), end='')
        print("|", end='')
        print(' ' * (n - 1), end='')
        print("|")
    else:
        print("|", end='')
        print("%s" % ('~' * (2*n+4)), end = '')
        print("|", end='')
        print(' ' * (n-1), end='')
        print("|")

print('=' * (3*n+5))

for j in range(0,n):
    print(' ' * j, end='')
    print("\\", end='')
    print("@" * (2*n+4-(2*j)), end='')
    print("/")

print('=' * (2*n+6))