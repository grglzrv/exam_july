cake = 45
wafer = 5.80
pancake = 3.20
count_days = int(input())
count_confectioner = int(input())
count_cake = int(input())
count_wafer = int(input())
count_pancake = int(input())

cake_c = count_cake * cake
wafer_c = count_wafer * float(wafer)
pancake_c = count_pancake * float(pancake)

total_price_per_day = (cake_c + wafer_c + pancake_c) * count_confectioner
total_sum_collect_entire_company = total_price_per_day * count_days
final_sum = total_sum_collect_entire_company - (total_sum_collect_entire_company / 8)
print(f'{final_sum:.2f}')
