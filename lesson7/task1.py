# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sort(arr, desc=False):
	last_unsorted = len(arr) - 1 # последний несорированный. все справа отсортированы
	last_sorted = 0 # последний, который сортировался
	i = 0
	while last_unsorted > 0:
		# print(arr)
		# print("i, sorted, unsorted: ", i, last_sorted, last_unsorted)
		if ( arr[i] < arr[i+1] if desc else arr[i] > arr[i+1] ):
			arr[i], arr[i+1] = arr[i+1], arr[i]
			last_sorted = i
		i += 1
		if i == last_unsorted:
			i = 0
			last_unsorted = last_sorted
			last_sorted = 0
	return arr


arr = [random.randint(-100, 99) for _ in range(10)]
print(bubble_sort(arr))
