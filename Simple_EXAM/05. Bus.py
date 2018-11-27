count_p = int(input())
count_taps = int(input())


p_ci = 0

for i in range(1, count_taps+1):
    p_co = int(input())

    if i % 2 == 1:
        count_p -= p_co
        p_ci = int(input())
        count_p = count_p + p_ci + 2
        continue

    if i % 2 == 0:

        count_p = (count_p - p_co) - 2
        p_ci = int(input())
        count_p += p_ci
        continue

print(f'The final number of passengers is : {count_p}')
