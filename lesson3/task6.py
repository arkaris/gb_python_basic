# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
arr = [randint(-5, 5) for _ in range(10)]
print("Исходный массив: ", arr)

index_min = index_max = 0
value_min = value_max = arr[0]
for i, item in enumerate(arr):
	if item < value_min:
		index_min = i
		value_min = item
	if item > value_max:
		index_max = i
		value_max = item

print(f"Минимальный и максиамльный элементы: ", value_min, value_max)

if -1 <= index_max - index_min <= 1:
	print("Между минимальным и максимальным элементом нет значений")
else:
	my_slice = arr[index_min + 1 : index_max] if index_min < index_max else arr[index_max + 1 : index_min]
	print("Сумма чисел между минимальным и максимальным элементом: ", sum(my_slice))
