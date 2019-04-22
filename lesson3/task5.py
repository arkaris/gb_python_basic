# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint
arr = [randint(-5, 5) for _ in range(10)]
print("Исходный массив: ", arr)

index = None
value = None
for i, item in enumerate(arr):
	if item < 0:
		if index is None or item > value:
			index = i
			value = item

if index is None:
	print("Отрицательных элементов нет")
else:
	print(f"Максимальный отрицательный элемент {value} расположен на {index} позиции")