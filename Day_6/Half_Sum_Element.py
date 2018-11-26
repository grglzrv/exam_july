n = int(input())

sum = 0
max_number = 0

for i in range(1, n+1):
    current_number = int(input())
    sum += current_number
    if i == 1:
        max_number = current_number
    if current_number > max_number:
        max_number = current_number
sum -= max_number
if max_number == sum:
    print(f'Yes\nSum = {sum}')
else:
    diff = abs(max_number - sum)
    print(f'No\nDiff = {diff}')


