# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from pympler import asizeof

import random as rnd
import math

begin, end = map(float, input("Введите через один пробел два числа: ").split(" "))
if begin > end:
	begin, end = end, begin

print(f"Границы заняли {asizeof.asizeof(begin)/8} и {asizeof.asizeof(end)/8} байт")

value = rnd.randint(math.floor(begin)+1, math.floor(end))
print("Случайное целое число: ", value)
print(f"Оно заняло {asizeof.asizeof(value)/8} байт")
value = rnd.uniform(begin, end)
print("Случайное дробное число: ", value)
print(f"Оно заняло {asizeof.asizeof(value)/8} байт")

begin, end = map((lambda s: s[0]), input("Введите через один пробел два символа: ").split(" "))
if (begin > end):
	begin, end = end, begin

print(f"Границы заняли {asizeof.asizeof(begin)/8} и {asizeof.asizeof(end)/8} байт")

value = chr(rnd.randint(ord(begin), ord(end)))
print("Случайный символ: ", value)
print(f"Он занял {asizeof.asizeof(value)/8} байт")
