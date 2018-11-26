price_ticket_co = float(input())
price_ticket_ci = float(input())
price_ticket_match = float(input())
match_count = int(input())
percent_discount = int(input())

sixth_fr_ticket_price = 6 * (price_ticket_co + price_ticket_ci)
discount = sixth_fr_ticket_price - (sixth_fr_ticket_price * (percent_discount / 100))
total_sum_ticket_match = 6 * match_count * price_ticket_match
total_sum = discount + total_sum_ticket_match
sum_fr = total_sum / 6

print(f'Total sum: {total_sum:.2f} lv.')
print(f'Each friend has to pay {sum_fr:.2f} lv.')