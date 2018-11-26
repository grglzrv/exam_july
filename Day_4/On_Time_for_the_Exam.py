exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minites = int(input())

exam_time = (exam_hour * 60) + exam_minutes
arrival_time = (arrival_hour * 60) + arrival_minites # vreme v minuti

late_time = arrival_time - exam_time
early_time = exam_time - arrival_time
hour = 0
minutes = 0

if (late_time <= 59) and (late_time > 0):
    print('late')
    print(f'{late_time} minutes after the start')
elif (late_time >= 60) and (late_time > 0):
    hour = late_time // 60
    minutes = late_time % 60
    print('Late')
    print(f'{hour}:{minutes:02d} hours after the start')
elif late_time == 0:
    print('On time')
elif (early_time <= 30) and (early_time > 0):
    print('On time')
    print(f'{early_time} minutes before the start')
elif (early_time > 30) and (early_time < 60):
    print('Early')
    print(f'{early_time} minutes before the start')
elif early_time >= 60:
    hour = early_time // 60
    minutes = early_time % 60
    print('Early')
    print(f'{hour}:{minutes:02d} hours before the start')