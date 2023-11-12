flag = False
while True:
    if flag == True:
        break
    age = int(input('Введите год рождения А.С. Пушкина :'))
    if age == 1799:
       while True:
           day = int(input('Введите день рождения А.С. Пушкина :'))
           if day == 6:
               flag = True
               break
print('Верно')