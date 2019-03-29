from random import randint
arr1 = [randint(1,21) for _ in range(10)]
print("Исходный массив: ", arr1)

# нахожу максимальный и минимальный индексы
min_index = 0
max_index = 0
for i, item in enumerate(arr1):
	if item < arr1[min_index]:
		min_index = i
	if item > arr1[max_index]:
		max_index = i

# меняю элементы местами
arr1[min_index], arr1[max_index] = arr1[max_index], arr1[min_index]
print("Результирующий массив: ", arr1)
