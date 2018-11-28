length = int(input())
width = int(input())
height = float(input())
pricePerMeter = float(input())
weigth = float(input())

perimeter = length*2 + width*2
wirePrice = perimeter*pricePerMeter
wireArea = perimeter*height
wireWeigth = wireArea*weigth

print(str(perimeter))
print("%.2f" % wirePrice)
print("%.3f" % wireWeigth)