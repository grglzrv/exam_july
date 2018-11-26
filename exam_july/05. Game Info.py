team = input()
count_matches = int(input())

total_minutes = 0
count_pen = 0
count_add_time = 0

for i in range(count_matches):
    match_duration = int(input())
    total_minutes += match_duration

    if match_duration > 120:
        count_pen += 1
    if (match_duration > 90) and (match_duration <= 120):
        count_add_time += 1

average_minutes = total_minutes / count_matches
print(f'{team} has played {total_minutes} minutes. Average minutes per game: {average_minutes:.2f}')
print(f'Games with penalties: {count_pen}')
print(f'Games with additional time: {count_add_time}')


