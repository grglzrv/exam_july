contract_period = input()
contract_type = input()
dessert = input()
count_months = int(input())

result = 0
total_result = 0

if contract_period == 'one':
    if contract_type == 'Small':
        if dessert == 'yes':
            result = 9.98 + 5.50
            total_result = result * count_months
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 9.98 * count_months
            print(f'{total_result:.2f} lv.')
    elif contract_type == 'Middle':
        if dessert == 'yes':
            result = 18.99 + 4.35
            total_result = result * count_months
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 18.99 * count_months
            print(f'{total_result:.2f} lv.')
    elif contract_type == 'Large':
        if dessert == 'yes':
            result = 25.98 + 4.35
            total_result = result * count_months
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 25.98 * count_months
            print(f'{total_result:.2f} lv.')
    elif contract_type == 'ExtraLarge':
        if dessert == 'yes':
            result = 35.99 + 3.85
            total_result = result * count_months
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 35.99 * count_months
            print(f'{total_result:.2f} lv.')
else:
    if contract_type == 'Small':
        if dessert == 'yes':
            result = 8.58 + 5.50
            total_result = result * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 8.58 * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
    elif contract_type == 'Middle':
        if dessert == 'yes':
            result = 17.09 + 4.35
            total_result = result * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 17.09 * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
    elif contract_type == 'Large':
        if dessert == 'yes':
            result = 23.59 + 4.35
            total_result = result * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 23.59 * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
    elif contract_type == 'ExtraLarge':
        if dessert == 'yes':
            result = 31.79 + 3.85
            total_result = result * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')
        else:
            total_result = 31.79 * count_months
            total_result = total_result - total_result * (3.75 / 100)
            print(f'{total_result:.2f} lv.')


