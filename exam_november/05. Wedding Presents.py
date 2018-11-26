guests = int(input())
n_gifts = int(input())

count_a = 0
count_b = 0
count_v = 0
count_g = 0

for i in range(1, n_gifts+1):
    text_input = input().upper()
    if text_input == 'A':
        count_a += 1
    elif text_input == 'B':
        count_b += 1
    elif text_input == 'V':
        count_v += 1
    elif text_input == 'G':
        count_g += 1

percent_money = (count_a / n_gifts) * 100
percent_el_device = (count_b / n_gifts) * 100
percent_vouchers = (count_v / n_gifts) * 100
percent_others = (count_g / n_gifts) * 100
percent_all = (n_gifts / guests) * 100

print(f'{percent_money:.2f}%')
print(f'{percent_el_device:.2f}%')
print(f'{percent_vouchers:.2f}%')
print(f'{percent_others:.2f}%')
print(f'{percent_all:.2f}%')
