# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# list = [1.1, 1.2, 3.1, 5, 10.01] # => 0.19

from random import randint

def createList():
    list = []
    for i in range(randint(5, 10)):
        list.append(randint(0, 9) + randint(0, 99) / 100)
    return list

def getDifference(list):
    newList = []
    for i in range(len(list)):
        if list[i]%1 != 0:
            newList.append(list[i]%1)
    return max(newList) - min(newList)

list = createList()
print(f'Cозданный список: {list}')
print(f'Разница дробных частей: {getDifference(list):.2f}')