# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(arr):
	len_arr = len(arr)
	if len_arr == 0 or len_arr == 1:
		return arr
	else:
		arr1 = merge_sort(arr[:len_arr//2])
		arr2 = merge_sort(arr[len_arr//2:])
		arr3 = []
		i, j = 0, 0
		for k in range(len_arr):
			if i > len(arr1) - 1:
				arr3.append(arr2[j])
				j += 1
			elif j > len(arr2) - 1:
				arr3.append(arr1[i])
			elif arr1[i] > arr2[j]:
				arr3.append(arr2[j])
				j += 1
			else:
				arr3.append(arr1[i])
				i += 1
		return arr3

arr = [random.uniform(-100, 99) for _ in range(10)]
print(merge_sort(arr))
