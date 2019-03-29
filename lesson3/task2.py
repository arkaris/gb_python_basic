from random import randint
arr1 = [randint(1,21) for _ in range(10)]
print("Исходный массив: ", arr1)

arr2 = []
for index, item in enumerate(arr1):
	if item % 2 == 0:
		arr2.append(index)

print("Индексы четных элементов", arr2)
