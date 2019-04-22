# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
arr = [randint(-5, 5) for _ in range(10)]
print("Исходный массив: ", arr)

sorted_arr = sorted(arr)
print("Два минимальных значения: ", sorted_arr[0], sorted_arr[1])