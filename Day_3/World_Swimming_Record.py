import math
world_record = float(input())
distance = float(input())
swimming_time = float(input())

ivancho_swimming_time = distance * swimming_time
water_resistance = math.floor(distance / 15) * 12.5

total_time = ivancho_swimming_time + water_resistance

if world_record > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    result = total_time - world_record
    print(f'No, he failed! He was {result:.2f} seconds slower.')



