count = float(input())
money = float(input())

c_count = 0
m_money = 0

while not c_count == count:

    if not (count <= 0 or money <= 0):
        m_money += money
        c_count += 1
        print(f"Increase: {money:.2f}")
        if not c_count == count:
            money = float(input())
    else:
        print("Invalid operation!")
        break

print(f"Total: {m_money:.2f}")
