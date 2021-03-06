def luckyTickets(num):
    array = [1] * 10 + [0] * (num // 2 * 9 - 9)
    for i in range(num // 2 - 1):
        array = [sum(array[x::-1]) if x < 10 else sum(array[x:x-10:-1]) for x in range(len(array))]
    return sum([x**2 for x in array])

# количество счастливых билетов среди шестизначных чисел
print(luckyTickets(6))
