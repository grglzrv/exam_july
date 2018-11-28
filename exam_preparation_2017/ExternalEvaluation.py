students = int(input())

poorCount = 0
satisfactoryCount = 0
goodCount = 0
veryGoodCount = 0
excellentCount = 0

for i in range(0, students):
    points = float(input())
    if points >= 0 and points < 22.5:
        poorCount += 1
    elif points >= 22.5 and points < 40.5:
        satisfactoryCount += 1
    elif points >= 40.5 and points < 58.5:
        goodCount += 1
    elif points >= 58.5 and points < 76.5:
        veryGoodCount += 1
    elif points >= 76.5 and points <= 100:
        excellentCount += 1

print('%.2f%% poor marks' % ((poorCount/students)*100))
print('%.2f%% satisfactory marks' % ((satisfactoryCount/students)*100))
print('%.2f%% good marks' % ((goodCount/students)*100))
print('%.2f%% very good marks' % ((veryGoodCount/students)*100))
print('%.2f%% excellent marks' % ((excellentCount/students)*100))