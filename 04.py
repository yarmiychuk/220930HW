# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def convertToBinary(number):
    bin = ''
    while number > 0:
        bin = str(number % 2) + bin
        number = number // 2
    return bin

binaryNum = convertToBinary(int(input('Введите число: ')))
print(f'Число в двоичной системе: {binaryNum}')