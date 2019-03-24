n = int(input("До какого числа проверять?: "))

my_sum = 0
success = True
for i in range(1, n+1):
	my_sum += i
	test_sum = i * (i + 1) / 2
	if test_sum != my_sum:
		success = False
	# Вывод в консоль замедляет работу
	# print(str(i), str(my_sum))

if success:
	print("Все сошлось!")
else:
	print("Где-то ошибка!")
