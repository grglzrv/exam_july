import time
bg_c = 1
usd_c = 1.79549
amount = float(input('Amount: '))
bgn = amount * usd_c / bg_c
print('Converting USD to BGN, please wait ...')
time.sleep(1)
print(f'{bgn:.2f} BGN')
