price_party = float(input())
count_love_msg = int(input())
count_wax_rose = int(input())
count_keychain = int(input())
count_caricatures = int(input())
count_surprise = int(input())

love_msg = 0.60
wax_rose = 7.2
keychain = 3.60
caricatures = 18.20
surprise = 22

total_sum = count_love_msg * love_msg + count_wax_rose * wax_rose + count_keychain * keychain + count_caricatures * caricatures + count_surprise * surprise
total_count = count_love_msg + count_wax_rose + count_keychain + count_caricatures + count_surprise
sum_discount = 0
sum_hosting = 0

if total_count >= 25:
    total_sum = total_sum - total_sum * (35 / 100)
    total_sum = total_sum - total_sum * (10 / 100)
else:
    total_sum = total_sum - total_sum * (10 / 100)
if total_sum > price_party:
    total_sum = total_sum - price_party
    print(f'Yes! {total_sum:.2f} lv left.')
else:
    total_sum = abs(total_sum - price_party)
    print(f'Not enough money! {total_sum:.2f} lv needed.')
