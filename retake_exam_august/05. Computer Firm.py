count_pc = int(input())

rate_counter = 0
total_sales = 0

for i in range(1, count_pc+1):
    number = input()
    num12 = ''
    num3 = ''
    num12 = number[-3:-1]
    num3 = number[-1:]

    rating = int(num3)
    sales = int(num12)
    rate_counter += rating

    if rating == 3:
        total_sales += int(sales * 0.50)
    elif rating == 4:
        total_sales += int(sales * 0.70)

    elif rating == 5:
        total_sales += int(sales * 0.85)

    elif rating == 6:
        total_sales += sales

average = rate_counter / count_pc
print(f'{total_sales:.2f}')
print(f'{average:.2f}')

