mm = 1000
cm = 100
mi = 0.000621371192
inch = 39.3700787
km = 0.001
ft = 3.2808399
yd = 1.0936133

num = float(input())
unit_from = input()
unit_to = input()

meters = 0
result = 0

if unit_from == 'mm':
    meters = num / mm
elif unit_from == 'cm':
    meters = num / cm
elif unit_from == 'mi':
    meters = num / mi
elif unit_from == 'in':
    meters = num / inch
elif unit_from == 'km':
    meters = num / km
elif unit_from == 'ft':
    meters = num / ft
elif unit_from == 'yd':
    meters = num / yd
else:
    meters = num

if unit_to == 'mm':
    result = meters * mm
elif unit_to == 'cm':
    result = meters * cm
elif unit_to == 'mi':
    result = meters * mi
elif unit_to == 'in':
    result = meters * inch
elif unit_to == 'km':
    result = meters * km
elif unit_to == 'ft':
    result = meters * ft
elif unit_to == 'yd':
    result = meters * yd
else:
    result = meters
print(f'{result:.8f}')
