# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import random as rnd
import math

begin, end = map(float, input("Введите через один пробел два числа: ").split(" "))
if begin > end:
	begin, end = end, begin

print("Случайное целое число: ", rnd.randint(math.floor(begin)+1, math.floor(end)))
print("Случайное дробное число: ", rnd.uniform(begin, end))

begin, end = map((lambda s: s[0]), input("Введите через один пробел два символа: ").split(" "))
if (begin > end):
	begin, end = end, begin

print("Случайный символ: ", chr(rnd.randint(ord(begin), ord(end))))