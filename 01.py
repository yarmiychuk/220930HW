# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def createList():
    list = []
    for i in range(randint(5, 15)):
        list.append(randint(0, 9))
    return list

def getSum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum

list = createList()
print(f'Созданный список: {list}')
print(f'Сумма элементов на нечётных позициях равна {getSum(list)}')