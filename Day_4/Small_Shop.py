product = input()
city = input()
quantity = float(input())
result = 0

if city.lower() == 'sofia':
    if product == 'coffee':
        result = quantity * 0.50
        print(result)
    elif product == 'water':
        result = quantity * 0.80
        print(result)
    elif product == 'beer':
        result = quantity * 1.20
        print(result)
    elif product == 'sweets':
        result = quantity * 1.45
        print(result)
    elif product == 'peanuts':
        result = quantity * 1.60
        print(result)
elif city.lower() == 'plovdiv':
    if product == 'coffee':
        result = quantity * 0.40
        print(result)
    elif product == 'water':
        result = quantity * 0.70
        print(result)
    elif product == 'beer':
        result = quantity * 1.15
        print(result)
    elif product == 'sweets':
        result = quantity * 1.30
        print(result)
    elif product == 'peanuts':
        result = quantity * 1.50
        print(result)
elif city.lower() == 'varna':
    if product == 'coffee':
        result = quantity * 0.45
        print(result)
    elif product == 'water':
        result = quantity * 0.70
        print(result)
    elif product == 'beer':
        result = quantity * 1.10
        print(result)
    elif product == 'sweets':
        result = quantity * 1.35
        print(result)
    elif product == 'peanuts':
        result = quantity * 1.55
        print(result)
