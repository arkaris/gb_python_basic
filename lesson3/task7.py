from random import randint
arr = [randint(-5, 5) for _ in range(10)]
print("Исходный массив: ", arr)

# min1 всегда меньше или равен min2
min1 = arr[0]
min2 = arr[1]
if min2 < min1:
	min1, min2 = min2, min1

for item in arr[2:]:
	if item < min2:
		min2 = item
	if min2 < min1:
		min1, min2 = min2, min1

print("Два минимальных значения: ", min1, min2)