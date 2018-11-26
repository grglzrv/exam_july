import math

time_brother_1 = float(input())
time_brother_2 = float(input())
time_brother_3 = float(input())
time_father = float(input())

work_time = 1 / (1 / time_brother_1 + 1 / time_brother_2 + 1 / time_brother_3)
break_time = work_time * 0.15
total_time = work_time + break_time
print(f'Cleaning time: {total_time:.2f}')

if total_time > time_father:
    not_enough_time = total_time - time_father
    print(f"No, there isn't a surprise - shortage of time -> {math.ceil(not_enough_time)} hours.")
else:
    enough_time = time_father - total_time
    print(f"Yes, there is a surprise - time left -> {math.floor(enough_time)} hours.")

