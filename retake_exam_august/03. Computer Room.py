months = input()
hours_taken = int(input())
count_people = int(input())
weather_day = input()

total_sum = 0

mon = {'day': {'march': 10.50, 'april': 10.50, 'may': 10.50, 'june': 12.60, 'july': 12.60, 'august': 12.60},
       'night': {'march': 8.40, 'april': 8.40, 'may': 8.40, 'june': 10.20, 'july': 10.20, 'august': 10.20}
       }

if count_people >= 4:
    mon[weather_day][months] = mon[weather_day][months] * 0.90
if hours_taken >= 5:
    mon[weather_day][months] = mon[weather_day][months] * 0.50

total_sum = hours_taken * mon[weather_day][months] * count_people
print(f'Price per person for one hour: {mon[weather_day][months]:.2f}')
print(f'Total cost of the visit: {total_sum:.2f}')
