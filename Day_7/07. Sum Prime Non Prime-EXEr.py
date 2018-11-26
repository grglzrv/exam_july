__author__ = "Georgi Lazarov"
__email__ = "lazarovgogo@gmail.com"

non_prime_sum = 0
prime_sum = 0

while True:
    prime_num = True
    num = input()

    if num == 'stop':
        break
    number = int(num)

    if number == 1:
        prime_num = False
    elif number < 0:
        print('Number is negative.')
        continue

    for i in range(2, number - 1):
        if number % i == 0:
            prime_num = False
            break
    if prime_num:
        prime_sum += number
    else:
        non_prime_sum += number
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
