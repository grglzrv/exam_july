n = int(input())

for i in range(1, 10):
    for m in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                sum = i + m
                if (sum == j+k) and n % sum == 0:
                    print("%d%d%d%d" % (i,m,j,k),
                          end=' ')

