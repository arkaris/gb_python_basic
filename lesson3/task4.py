from random import randint
arr = [randint(0, 1) for _ in range(4)]
print("Исходный массив: ", arr)

# Предположим, что в массиве могут лежать дробные числа
# Использовать словарь нельзя

# Буду в цикле
# удалять элементы из массива так,
# что если в нем есть два или более одинаковых элемента, то удалится один из них
# пока в массиве не останется один элемент.
# Отдельно нужно учесть случай,
# когда несколько разных элементов встречаются одинковое количество раз,
# тогда при последнем срезе массив останется пустым.

tmp = arr.copy()
while len(tmp) > 0:
	result = tmp
	deleted = []
	def is_deleted(item):
		if item in deleted:
			return True
		else:
			deleted.append(item)
			return False
	tmp = list(filter(is_deleted, tmp))
	# print("*"*10)
	# print(result)
	# print(tmp)

if len(result) == len(arr):
	print("Все элементы массива встречаются по 1 разу")
elif len(result) == 1:
	print("В исходном массиве чаще всего встречается элемент ", result[0])
else:
	print("В исходном массиве чаще всего встречаются элементы ", ", ".join(map(str, result)))

# При первом тесте на большом массиве [randint(0, 110) for _ in range(4000)] ответ был 42
# что бы это ни значило