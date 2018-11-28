import math

tomatoes = float(input())
boxes = int(input())
jarsPerBox = int(input())

liutenica = tomatoes/5
print("Total lutenica: %d kilograms." % math.floor(liutenica))

jarsFilled = liutenica/0.535
boxFilled = jarsFilled/jarsPerBox

if boxFilled >= boxes:
    boxesLeft = boxFilled-boxes
    print("%d boxes left." % boxesLeft)
    print("%d jars left." % (boxesLeft*jarsPerBox))
else:
    boxesNeeded = boxes - boxFilled
    print("%d more boxes needed." % boxesNeeded)
    print("%d more jars needed." % (boxesNeeded*jarsPerBox))