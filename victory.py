while True:
   answer = 0
    # 1799
   age = int(input('Введите год рождения А.С. Пушкина :'))
   if age == 1799:
        answer += 1
   # 1809
   age = int(input('Введите год рождения Н.В. Гоголя :'))
   if age == 1809:
        answer += 1
    # 1814
   age = int(input('Введите год рождения М.Ю. Лермонтов :'))
   if age == 1814:
        answer += 1
    # 1867
   age = int(input('Введите год рождения К.Д. Бальмонтаа :'))
   if age == 1867:
        answer += 1
    #1828
   age= int(input('Введите год рождения Л.Н. Толстого :'))
   if age == 1828: answer += 1
   print("Количество правильных ответов : ", answer)
   print("Количество ошибок : ", 5 - answer)
   print("Процент правильных ответов : ", answer*100/5)
   print("Процент ошибок : ", (5-answer)*100/5)
   if input('Хотите начать сначала : ') != 'да':
      break
print('Конец игры')