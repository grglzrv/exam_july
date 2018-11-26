magic_number = int(input())

for first in range(0, 10):
    for second in range(0, 10):
        for third in range(0, 10):
            for fourth in range(0, 10):
                for fifth in range(0, 10):
                    for sixth in range(0, 10):
                        if first*second*third*fourth*fifth*sixth == magic_number:
                            print(f'{first}{second}{third}{fourth}{fifth}{sixth} ', end='')
