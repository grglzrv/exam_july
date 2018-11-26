import math

year_type = input()
holidays_count = int(input())
weekends_count = int(input())

days_sofia = 48 - weekends_count
days_sofia *= 3.0 / 4
holidays = holidays_count * (2.0 / 3)

total_days = days_sofia + holidays + weekends_count
result = 0
if year_type == 'leap':
    result = total_days + (total_days * 15 / 100)
    print(f'{math.floor(result)}')
else:
    print(f'{math.floor(total_days)}')




