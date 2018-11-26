years = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())

sum_per_birthday = 0
saved_money = 0

toys = 0
money_for_brother = 0

for birthday in range(1, years+1):
    if birthday % 2 == 0:
        sum_per_birthday += 10
        saved_money += sum_per_birthday
        money_for_brother += 1
    else:
        toys += 1

saved_money = saved_money + price_per_toy*toys - money_for_brother
if saved_money >= price_washing_machine:
    result = saved_money - price_washing_machine
    print(f'Yes! {result:.2f}')
else:
    diff = saved_money - price_washing_machine
    print(f'No! {abs(diff):.2f}')
