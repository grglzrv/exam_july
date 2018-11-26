steps_count = int(input())
dancers_count = int(input())
days_count = int(input())

steps_per_day = ((steps_count / days_count) / steps_count) * 100
dancer_steps = steps_per_day / 20

if steps_per_day <= 13:
    print(f'Yes, they will succeed in that goal! {dancer_steps}%.')
else:
    print(f'No, They will not succeed in that goal! Required {dancer_steps}% steps to be learned per day.')
