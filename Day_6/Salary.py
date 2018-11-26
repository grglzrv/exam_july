n_tabs = int(input())
salary = float(input())

final_salary = 0

for i in range(1, n_tabs + 1):
    website_tab = input()
    if website_tab == 'Facebook':
        salary -= 150
        if salary == 0:
            print('You have lost your salary.')
            break
    else:
        if (website_tab != 'Facebook') and (website_tab != 'website_tab') and (website_tab != 'Reddit'):
            final_salary = salary

    if website_tab == 'Instagram':
        salary -= 100
        if salary == 0:
            print('You have lost your salary.')
            break
    else:
        if (website_tab != 'Facebook') and (website_tab != 'website_tab') and (website_tab != 'Reddit'):
            final_salary = salary
    if website_tab == 'Reddit':
        salary -= 50
        if salary == 0:
            print('You have lost your salary.')
            break
    else:
        if (website_tab != 'Facebook') and (website_tab != 'website_tab') and (website_tab != 'Reddit'):
            final_salary = salary

if salary > 0:
    print(int(salary))

