n = input()

for i in reversed(n):
    if i == '0':
        print('ZERO')
    else:
        symbol = int(i) + 33
        symbol = chr(symbol)
        print(symbol*int(i))