price_c = float(input())
puzzles_c = int(input())
dolls_c = int(input())
teddy_bears_c = int(input())
minions_c = int(input())
tracks_c = int(input())

sum = puzzles_c*2.60 + dolls_c*3 + teddy_bears_c*4.10 + minions_c*8.20 + tracks_c*2
toys = puzzles_c + dolls_c + teddy_bears_c + minions_c + tracks_c

if toys >= 50:
    sum = sum - sum*0.25

rent = sum*0.1
sum = sum - rent

if sum >= price_c:
    diff = sum - price_c
    print(f'Yes! {diff:.2f} lv left.')
else:
    diff = price_c - sum
    print(f'Not enough money! {diff:.2f} lv needed.')





