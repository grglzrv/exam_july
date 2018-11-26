n1 = int(input())
n2 = int(input())
n_operator = input()

result = 0

if n2 == 0 and (n_operator == '/' or n_operator == '%'):
    print(f'Cannot divide {n1} by zero')
elif n_operator == '/':
    result = n1 / n2
    print(f'{n1} {n_operator} {n2} = {result:.2f}')
elif n_operator == '%':
    result = n1 % n2
    print(f'{n1} {n_operator} {n2} = {result}')
else:
    if n_operator == '+':
        result = n1 + n2
        if result % 2 == 0:
            print(f'{n1} {n_operator} {n2} = {result} - even')
        else:
            print(f'{n1} {n_operator} {n2} = {result} - odd')
    elif n_operator == '-':
        result = n1 - n2
        if result % 2 == 0:
            print(f'{n1} {n_operator} {n2} = {result} - even')
        else:
            print(f'{n1} {n_operator} {n2} = {result} - odd')
    elif n_operator == '*':
        result = n1 * n2
        if result % 2 == 0:
            print(f'{n1} {n_operator} {n2} = {result} - even')
        else:
            print(f'{n1} {n_operator} {n2} = {result} - odd')

