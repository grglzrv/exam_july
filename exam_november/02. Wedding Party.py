count_guests = int(input())
budged = int(input())

covert_per_people = 20
fireworks_money = 0
donation_money = 0
sum_covert = covert_per_people * count_guests

if budged >= sum_covert:
    budged -= sum_covert
    fireworks_money = round(budged * (40 / 100))
    donation_money = round(budged - fireworks_money)
    print(f'Yes! {fireworks_money} lv are for fireworks and {donation_money} lv are for donation.')
else:
    needed_money = round(sum_covert - budged)
    print(f'They won\'t have enough money to pay the covert. They will need {needed_money} lv more.')
