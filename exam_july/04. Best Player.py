name = input()

winner_name = ''
current_winner_goals = 0

while not name == 'END':
    goals = int(input())
    if goals > current_winner_goals:
        current_winner_goals = goals
        winner_name = name
    if current_winner_goals >= 10:
        break
    name = input()

print(f'{winner_name} is the best player!')

if goals >= 3:
    print(f'He has scored {current_winner_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {current_winner_goals} goals.')
