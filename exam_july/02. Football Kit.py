t_shirt_price = float(input())
sum_goal = float(input())

price_shorts = t_shirt_price * (75 / 100)
price_socks = price_shorts * (20 / 100)
price_buttons = (t_shirt_price + price_shorts) * 2
total_sum = t_shirt_price + price_shorts + price_socks + price_buttons
sum_after_discount = total_sum - (total_sum * (15 / 100))

if sum_after_discount >= sum_goal:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {sum_after_discount:.2f} lv.')
else:
    money_needed = abs(sum_after_discount - sum_goal)
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {money_needed:.2f} lv. more.')