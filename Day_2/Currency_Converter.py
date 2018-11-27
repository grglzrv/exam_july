bgn_c = 1
usd_c = 1.79549
eur_c = 1.95583
gbp_c = 2.53405
amount = float(input('Amount: '))
convert_from = input('From: ')
convert_to = input('To: ')

if convert_from == 'BGN':
    if convert_to == 'USD':
        usd = amount * bgn_c / usd_c
        print(f'{usd:.2f} USD')
    elif convert_to == 'EUR':
        eur = amount * bgn_c / eur_c
        print(f'{eur:.2f} EUR')
    elif convert_to == 'GBP':
        gbp = amount * bgn_c / gbp_c
        print(f'{gbp:.2f} GBP')
    else:
        print('Wrong Convert To: value')
else:
    print('Wrong Convert From: value')

if convert_from == 'USD':
    if convert_to == 'BGN':
        bgn = amount * usd_c / bgn_c
        print(f'{bgn:.2f} BGN')
    elif convert_to == 'EUR':
        eur = amount * usd_c / eur_c
        print(f'{eur:.2f} EUR')
    elif convert_to == 'GBP':
        gbp = amount * usd_c / gbp_c
        print(f'{gbp:.2f} GBP')
    else:
        print('Wrong Convert To: value')
else:
    print('Wrong Convert From: value')

if convert_from == 'EUR':
    if convert_to == 'USD':
        usd = amount *eur_c / usd_c
        print(f'{usd:.2f} USD')
    elif convert_to == 'BGN':
        bgn = amount * eur_c / bgn_c
        print(f'{bgn:.2f} BGN')
    elif convert_to == 'GBP':
        gbp = amount * eur_c / gbp_c
        print(f'{gbp:.2f} GBP')
    else:
        print('Wrong Convert To: value')
else:
    print('Wrong Convert From: value')

if convert_from == 'GBP':
    if convert_to == 'USD':
        usd = amount * gbp_c / usd_c
        print(f'{usd:.2f} USD')
    elif convert_to == 'EUR':
        eur = amount * gbp_c / eur_c
        print(f'{eur:.2f} EUR')
    elif convert_to == 'BGN':
        bgn = amount *gbp_c / bgn_c
        print(f'{bgn:.2f} BGN')
    else:
        print('Wrong Convert To: value')
else:
    print('Wrong Convert From: value')

