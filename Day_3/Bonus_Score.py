num = float(input())
bonus = 0

if num <= 100:
    bonus += 5
elif 100 < num <= 1000:
    bonus = num * 20 / 100
elif num > 1000:
    bonus = num * 10 / 100

if num % 2 == 0:
    bonus += 1
elif num % 5 == 0:
    bonus += 2

print(bonus)
total_score = bonus + num
print(total_score)
