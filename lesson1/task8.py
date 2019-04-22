# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int( input("Введите номер года: ") )

if year % 400 == 0:
	isLeap = True
elif year % 100 == 0:
	isLeap = False
else:
	isLeap = year % 4 == 0

if isLeap:
	print("Выбранный год високосный")
else:
	print("Выбранный год не високосный")