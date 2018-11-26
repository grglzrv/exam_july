ml = float(input())
but = input()


but_sum = 0
count = 0

while not (but_sum == ml or but_sum > ml):
    count += 1
#    but = input()
    if but == 'Easy':
        but_sum += 50
    elif but == 'Medium':
        but_sum += 100
    else:
        but_sum += 200

    if but_sum < ml:
        but = input()

if but_sum == ml:
    print(f"The dispenser has been tapped {count} times.")
else:
    print(f"{int(but_sum - ml)}ml has been spilled.")
