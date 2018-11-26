minutes = int(input())
name = input()

if minutes == 0:
    print('Match has just began!')
elif minutes < 45:
    print('First half time.')
elif minutes >= 45:
    print('Second half time.')
if minutes >= 1 and (minutes <= 10):
    print(f'{name} missed a penalty.')
    if minutes % 2 == 0:
        print(f'{name} was injured after the penalty.')
elif minutes > 10 and (minutes <= 35):
    print(f'{name} received yellow card.')
    if minutes % 2 == 1:
        print(f'{name} got another yellow card.')
elif (minutes > 35) and minutes < 45:
    print(f'{name} SCORED A GOAL !!!')
elif minutes > 45 and (minutes < 55):
    print(f'{name} got a freekick.')
    if minutes % 2 == 0:
        print(f'{name} missed the freekick.')
elif minutes > 55 and (minutes <= 80):
    print(f'{name} missed a shot from corner.')
    if minutes % 2 == 1:
        print(f'{name} has been changed with another player.')
elif minutes > 80 and (minutes <= 90):
    print(f'{name} SCORED A GOAL FROM PENALTY !!!')