n = int(input())

oddSum = 0
oddMin = 'No'
oddMax = 'No'
evenSum = 0
evenMin = 'No'
evenMax = 'No'

for i in range(1, n + 1):
    current_number = float(input())

    if i % 2 == 0:
        evenSum += current_number
        if evenMin == 'No':
            evenMin = current_number
            evenMax = current_number
        if evenMin > current_number:
            evenMin = current_number
        if current_number > evenMax:
            evenMax = current_number
    else:
        oddSum += current_number
        if oddMin == 'No':
            oddMin = current_number
            oddMax = current_number
        if oddMin > current_number:
            oddMin = current_number
        if current_number > oddMax:
            oddMax = current_number

if oddMin == 'No':
    print(f'OddSum = {oddSum}')
    print(f'OddMin = {oddMin}')
    print(f'OddMax = {oddMax}')
else:
    print(f'OddSum = {oddSum:.2f}'.rstrip('0').rstrip('.'))
    print(f'OddMin = {oddMin:.2f}'.rstrip('0').rstrip('.'))
    print(f'OddMax = {oddMax:.2f}'.rstrip('0').rstrip('.'))

if evenMin == 'No':
    print(f'evenSum = {evenSum}')
    print(f'evenMin = {evenMin}')
    print(f'evenMax = {evenMax}')
else:
    print(f'evenSum = {evenSum:.2f}'.rstrip('0').rstrip('.'))
    print(f'evenMin = {evenMin:.2f}'.rstrip('0').rstrip('.'))
    print(f'evenMax = {evenMax:.2f}'.rstrip('0').rstrip('.'))


