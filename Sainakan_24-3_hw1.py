'''
Домашнее задание № 1
Написать программу для вычисления среднего показателя температуры воздуха в Кыргызстане на сегодня.

1) Температура каждой области должна вводиться пользователем по запросу программы.
2) Средний показатель должен быть в виде числа с плавающей точкой с одной цифрой после точки (float).
3) Применить конкатенацию или любое другое форматирование строк, но Введение в Python: Встроенные функции, переменные, комментарии.
4)Базовые типы данных: строки, целые и дробные числа.вывод данных должен быть например в таком формате:
Средний показатель температуры воздуха по КР на сегодня 24.8 °C.
'''
T_Сhui = float(input('введите температуру Чуйской Области: '))
T_N = float(input('введите температуру Нарынской Области: '))
T_IK = float(input('введите температуру Иссы-Кульской Области: '))
T_Osh = float(input('введите температуру Ошской Области: '))
T_JA = float(input('введите температуру Джалабадской Области: '))
T_Bn = float(input('введите температуру Баткенской Области: '))
T_Tl = float(input('введите температуру Таласской Области: '))

sum_temperature = T_Сhui + T_N + T_IK + T_Osh + T_JA + T_Bn + T_Tl
temperature_quantity = 7 #т.к. всего 7 областей
temperature_average = round(sum_temperature / temperature_quantity, 1) # 1, т.к. показательно нужно вывести десятых.
print(f'Средний показатель температуры воздуха по КР на сегодня: {temperature_average}°C.' )