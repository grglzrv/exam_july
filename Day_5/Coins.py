money = float(input())

coins = 0

stotinki = money * 100
counter = 0

while stotinki >= 200:
    stotinki = int(stotinki) - 200
    counter +=1

while stotinki >= 100:
    stotinki = int(stotinki) - 100
    counter += 1

while stotinki >= 50:
    stotinki = int(stotinki) - 50
    counter += 1

while stotinki >= 20:
    stotinki = int(stotinki) - 20
    counter += 1

while stotinki >= 10:
    stotinki = int(stotinki) - 10
    counter += 1

while stotinki >= 5:
    stotinki = int(stotinki) - 5
    counter += 1

while stotinki >= 2:
    stotinki = int(stotinki) - 2
    counter += 1

while stotinki >= 1:
    stotinki = int(stotinki) - 1
    counter += 1

print(counter)
