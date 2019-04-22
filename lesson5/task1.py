 # Пользователь вводит данные о количестве предприятий,
 # их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
 # Программа должна определить среднюю прибыль (за год для всех предприятий) и
 # вывести наименования предприятий, чья прибыль выше среднего и
 # отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

factory_count = int(input("Введите количесво предприятий: "))

factories = []
Factory = namedtuple("Factory", ["name", "q1", "q2", "q3", "q4", "total"])
for i in range(factory_count):
	print()
	name = input(f"Введите название предприятия {i+1}: ")
	q1 = float(input("Введите доход за первый квартал: "))
	q2 = float(input("Введите доход за второй квартал: "))
	q3 = float(input("Введите доход за третий квартал: "))
	q4 = float(input("Введите доход за четвертый квартал: "))
	total = sum((q1, q2, q3, q4))
	factories.append(Factory(name, q1, q2, q3, q4, total))

print()

common_avg = sum(map(lambda f: f.total, factories)) / len(factories) / 4
print(f"Средний доход за квартал по всем предприятиям: {common_avg}")

higher = []
lower = []
for factory in factories:
	if factory.total / 4 < common_avg:
		lower.append(factory)
	else:
		higher.append(factory)
print("Предприятия с прибылью выше среднего: ")
for factory in higher:
	print(f"Предприятие {factory.name} имеет средний доход {factory.total / 4}")
print("Предприятия с прибылью ниже среднего: ")
for factory in lower:
	print(f"Предприятие {factory.name} имеет средний доход {factory.total / 4}")