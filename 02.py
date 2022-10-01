# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

def createList():
    list = []
    for i in range(randint(5, 10)):
        list.append(randint(0, 9))
    return list

def getMultiplications(list):
    newList = []
    i = 0
    while i < len(list) / 2:
        newList.append(list[i] * list[len(list) - 1 - i])
        i += 1

    return newList

list = createList()
print(f'Созданный список: {list}')
print(f'Результаты перемножения пар элементов: {getMultiplications(list)}')