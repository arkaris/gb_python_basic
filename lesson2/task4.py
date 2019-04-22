# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
# ...Количество элементов (n) вводится с клавиатуры.

n = int(input("Введите число элементов ряда: "))

next_elem = 1.
my_sum = 0
for i in range(n):
	my_sum += next_elem
	next_elem = -next_elem
	next_elem /= 2

print(my_sum)