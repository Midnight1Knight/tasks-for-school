string = list(str(input())) #Вводим строку
j = 0
while j != 2: #Сколько раз шифруем(у меня шифруется 2 раза)
    middle = string[0] #Запоминается первое число
    for i in range(0, len(string)):
        if i + 1 == len(string): #Если осталось перебрать только последнее число
            string[i] = middle
            print(string[i])
            print()
            break
        string[i] = string[i + 1] #Перебираем все числа
        print(string[i], end=" ")
    j += 1
