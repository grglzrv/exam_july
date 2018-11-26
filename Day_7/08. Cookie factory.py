sum_letters = 0
max_sum_letters = 0
winner_name = None

while True:
    name = input()
    if name == 'STOP':
        break
    for letter in name:
        sum_letters += ord(letter)
        if max_sum_letters < sum_letters:
            max_sum_letters = sum_letters
            winner_name = name
    sum_letters = 0
print(f'Winner is {winner_name} - {max_sum_letters}!')
