# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def getList(num):
    list = [-1, 1, 0, 1, 1]
    for i in range(2, num):
        list.append(list[len(list) - 1] + list[len(list) - 2])
        list.insert(0, list[1] - list[0])
    return list

list = getList(int(input('Введите число: ')))
print(f'Список чисел Фибоначчи: {list}')