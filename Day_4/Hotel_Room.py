month = input()
nights = int(input())

studio_rent = 0
apartment_rent = 0
total_price_studio = 0
total_price_apartment = 0

if month == 'May' or month == 'October':
    studio_price = 50.00
    apartment_price = 65.00
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        total_price_apartment = apartment_rent - (apartment_rent * 10 / 100)
        total_price_studio = studio_rent - (studio_rent * 30 / 100)
        print(f'Apartment: {total_price_apartment:.2f} lv.')
        print(f'Studio: {total_price_studio:.2f} lv.')
    elif (nights > 7) and (nights <= 14):
        total_price_studio = studio_rent - (studio_rent * 5 / 100)
        print(f'Apartment: {apartment_rent:.2f} lv.')
        print(f'Studio: {total_price_studio:.2f} lv.')
    elif nights <= 7:
        print(f'Apartment: {apartment_rent:.2f} lv.')
        print(f'Studio: {studio_rent:.2f} lv.')
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        total_price_apartment = apartment_rent - (apartment_rent * 10 / 100)
        total_price_studio = studio_rent - (studio_rent * 20 / 100)
        print(f'Apartment: {total_price_apartment:.2f} lv.')
        print(f'Studio: {total_price_studio:.2f} lv.')
    elif nights <= 14:
        print(f'Apartment: {apartment_rent:.2f} lv.')
        print(f'Studio: {studio_rent:.2f} lv.')
else:
    if month == 'July' or month == 'August':
        studio_price = 76.00
        apartment_price = 77.00
        studio_rent = studio_price * nights
        apartment_rent = apartment_price * nights
        if nights > 14:
            total_price_apartment = apartment_rent - (apartment_rent * 10 / 100)
            print(f'Apartment: {total_price_apartment:.2f} lv.')
            print(f'Studio: {studio_rent:.2f} lv.')
        elif nights <= 14:
            print(f'Apartment: {apartment_rent:.2f} lv.')
            print(f'Studio: {studio_rent:.2f} lv.')
