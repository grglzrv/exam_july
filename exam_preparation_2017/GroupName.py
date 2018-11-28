capitalLetter = input()
lowerLetter1 = input()
lowerLetter2 = input()
lowerLetter3 = input()
digit = int(input())

if n == 5:
    print()

count = 0
for i in range(65, ord(capitalLetter)+1):
    for n in range(97, ord(lowerLetter1)+1):
        for m in range(97, ord(lowerLetter2)+1):
            for j in range(97, ord(lowerLetter3)+1):
                for k in range(0, digit+1):
                    count += 1

print(count-1)
