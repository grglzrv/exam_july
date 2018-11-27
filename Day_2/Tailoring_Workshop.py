usd_c = 1.85
c_table = int(input('Count of tables: '))
l_table = float(input('Length of tables in meters: '))
w_table = float(input('Width of tables in meters: '))

area_cover = c_table * (l_table + 2 * 0.30) * (w_table + 2 * 0.30)
area_square = c_table * (l_table / 2) * (l_table / 2)

usd = (area_cover * 7) + (area_square * 9)
print(f'Price in USD is: {usd:.2f} USD')

bgn = usd * usd_c
print(f'Price in GBN is: {bgn:.2f} BGN')
