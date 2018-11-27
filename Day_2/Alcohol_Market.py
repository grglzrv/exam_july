p_whiskey = float(input())
v_beer = float(input())
v_wine = float(input())
v_raki = float(input())
v_whiskey = float(input())

price_raki = p_whiskey / 2
price_wine = price_raki - (0.4 * price_raki)
price_beer = price_raki - (0.8 * price_raki)
sum_raki = v_raki * price_raki
sum_wine = v_wine * price_wine
sum_beer = v_beer * price_beer
sum_whiskey = v_whiskey * p_whiskey
total_sum = sum_raki + sum_wine + sum_beer + sum_whiskey
print(f'{total_sum:.2f}')
