second1 = int(input())
second2 = int(input())
second3 = int(input())

total_sec = second1 + second2 + second3
minutes = total_sec // 60
seconds = 0

if 10 <= total_sec <= 59:
    seconds = total_sec
    print(f'{minutes}:{seconds:02d}')
elif 60 <= total_sec <= 119:
    seconds = total_sec - 60
    print(f'{minutes}:{seconds:02d}')
elif 120 <= total_sec <= 179:
    seconds = total_sec - 120
    print(f'{minutes}:{seconds:02d}')
else:
    seconds = total_sec % 60
    print(f'{minutes}:{seconds:02d}')
