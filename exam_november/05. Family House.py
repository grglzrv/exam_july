n_months = int(input())

sum_electricity = 0
sum_water = n_months * 20
sum_internet = n_months * 15

water = 20
internet = 15
other = 0
total_other = 0

for i in range(n_months):
    electricity_bill = float(input())
    sum_electricity += electricity_bill
    other = (electricity_bill + 35) + ((electricity_bill + 35) * 0.20)
    total_other += other

month_average = (sum_electricity + sum_water + sum_internet + total_other) / n_months
print(f'Electricity: {sum_electricity:.2f} lv')
print(f'Water: {sum_water:.2f} lv')
print(f'Internet: {sum_internet:.2f} lv')
print(f'Other: {total_other:.2f} lv')
print(f'Average: {month_average:.2f} lv')




