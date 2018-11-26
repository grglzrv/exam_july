price_whiskey = float(input())
water_quantity = float(input())
wine_quantity = float(input())
champagne_quantity = float(input())
whiskey_quantity = float(input())

price_champagne = price_whiskey * (50 / 100)
price_wine = price_champagne * (40 / 100)
price_water = price_champagne * (10 / 100)
sum_champagne = champagne_quantity * price_champagne
sum_wine = wine_quantity * price_wine
sum_water = water_quantity * price_water
sum_whiskey = whiskey_quantity * price_whiskey
total_sum = sum_champagne + sum_wine + sum_water + sum_whiskey
print(f'{total_sum:.2f}')
