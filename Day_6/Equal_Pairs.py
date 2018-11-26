n = int(input())

previous_sum = 0
current_sum = 0
max_diff = 0

for i in range(1, n + 1):
    num1 = int(input())
    num2 = int(input())

    if i == 1:
        previous_sum = num1 + num2
    else:
        current_sum = num1 + num2
        current_diff = abs(previous_sum - current_sum)
        if current_diff > max_diff:
            max_diff = current_diff
        previous_sum = current_sum

if max_diff == 0:
    print(f'Yes, value={previous_sum}')
else:
    print(f'No, maxdiff={max_diff}')
