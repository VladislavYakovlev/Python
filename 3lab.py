import math
import random

print("\tИмя\t\t\tДействие")
print()
print("\t+\t\t\tСложение")  # \t - отступ
print("\t-\t\t\tВычитание")
print("\t*\t\t\tУмножение")
print("\t/\t\t\tДеление")
print("\tСТЕПЕНЬ\t\tВозведение в степень")
print("\tМОДУЛЬ\t\tМодуль числа")
print("\tРАНДОМ\t\tСлучайное число от 0 до 1")
print("\tФАКТОРИАЛ\tФакториал числа")
print("\tАРККОСИНУС\t\tАрккосинус")
print("\tВЫЙТИ\t\tВыйти")

while True:
    operation = str(input("Введите имя операции: "))
    if operation == '+':
        chis1 = float(input("Первое число: "))
        chis2 = float(input("Второе число: "))
        print("{} + {} = {}".format(chis1, chis2, chis1 + chis2))
    elif operation == '-':
        chis1 = float(input("Первое число: "))
        chis2 = float(input("Второе число: "))
        print("{} - {} = {}".format(chis1, chis2, chis1 - chis2))
    elif operation == '*':
        chis1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
        print("{} * {} = {}".format(chis1, chis2, chis1 * chis2))
    elif operation == '/':
        chis1 = float(input("Первое число: "))
        chis2 = float(input("Второе число: "))
        print("{} / {} = {}".format(chis1, chis2, chis1 / chis2))
    elif operation == 'СТЕПЕНЬ' or operation == 'Степень' or operation == 'степень':
        chis1 = float(input("Основание: "))
        chis2 = float(input("Степень: "))
        print("{} ^ {} = {}".format(chis1, chis2, chis1 ** chis2))
    elif operation == 'МОДУЛЬ' or operation == 'Модуль' or operation == 'модуль':
        chis = float(input("Число: "))
        print("|{}| = {}".format(chis, abs(chis)))
    elif operation == 'РАНДОМ' or operation == 'Рандом' or operation == 'рандом':
        print("Случайное число - {}".format(random.random()))
    elif operation == 'ФАКТОРИАЛ' or operation == 'Факториал' or operation == 'факториал':
        chis = int(input("Число (только натуральное и ноль): "))
        if chis >= 0:
            print("{}! = {}".format(chis, math.factorial(chis)))
        else:
            print("Ошибка!")
    elif operation == 'АРККОС' or operation == 'Арккос' or operation == 'арккос':
        chis = float(input("Число от -1 до 1: "))
        if (chis <= 1) and (chis >= -1):
            print("arccos({}) = {}".format(chis, math.acos(chis)))
        else:
            print("Ошибка!")
    elif operation == 'ВЫЙТИ' or operation == 'Выйти' or operation == 'выйти':
        break
    else:
        print("Нет такой операции!")
