weight = float(input())
serviceType = input()
distance = int(input())

pricePerKm = 0
if weight < 1:
    pricePerKm = 0.03
elif weight >= 1 and weight <= 10:
    pricePerKm = 0.05
elif weight >= 11 and weight <= 40:
    pricePerKm = 0.1
elif weight >= 41 and weight <= 90:
    pricePerKm = 0.15
elif weight >= 91 and weight <= 150:
    pricePerKm = 0.20

if serviceType == "express":
    if weight < 1:
        pricePerKm = pricePerKm + (0.8 * pricePerKm)*weight
    elif weight >= 1 and weight <= 10:
        pricePerKm = pricePerKm + (0.4 * pricePerKm)*weight
    elif weight >= 11 and weight <= 40:
        pricePerKm = pricePerKm + (0.05 * pricePerKm)*weight
    elif weight >= 41 and weight <= 90:
        pricePerKm = pricePerKm + (0.02 * pricePerKm)*weight
    elif weight >= 91 and weight <= 150:
        pricePerKm = pricePerKm + (0.01 * pricePerKm)*weight

price = pricePerKm * distance

print("The delivery of your shipment with weight of %.3f kg. "
      "would cost %.2f lv." % (weight, price))