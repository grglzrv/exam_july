days = int(input())
dancers = int(input())

sumEnergy = 0
for i in range(1, days+1):
    hoursTrained = int(input())
    if (i % 2 == 0) and (hoursTrained % 2 == 0):
        # sumEnergy = sumEnergy + (dancers * 68)
        sumEnergy += dancers * 68
    elif (i % 2 == 1) and (hoursTrained % 2 == 0):
        sumEnergy += dancers * 49
    elif (i % 2 == 0) and (hoursTrained % 2 == 1):
        sumEnergy += dancers * 65
    elif (i % 2 == 1) and (hoursTrained % 2 == 1):
        sumEnergy += dancers * 30

overallEnergy = days * dancers * 100
energyLeft = overallEnergy - sumEnergy
energyLeftPerDancer = energyLeft / dancers
energyLeftPerDay = energyLeftPerDancer / days

if energyLeftPerDay > 50:
    print("They feel good! Energy left: %.2f" % energyLeftPerDay)
else:
    print("They are wasted! Energy left: %.2f" % energyLeftPerDay)