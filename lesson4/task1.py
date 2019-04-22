# Написать два алгорима выполняющих одну и ту же задачу и проверить с помощью модуля timeit, какой работает быстрее.

import timeit
import math

# Числа Фибоначи на неоптимизированной рекурсии со счетчиком вызовов
def fib_recur_with_counter(k):
	counter_recur[k] += 1
	if k < 1: 
		return k + 1
	else:
		return fib_recur_with_counter(k - 1) + fib_recur_with_counter(k - 2)

# for n in range(3, 20):
# 	counter_recur = [0] * (n+1)
# 	fib_recur_with_counter(n)
# 	print(sum(counter_recur))
# 	print(math.pow(1.66,n))
# 	print("*"*5)
# exit()

'''
Вывод:
Каждый вызов такой функции делает 2 новых вызова
С каждым n число вызовов рестет с геометрической прогрессией, что и приводит
'''

# Числа Фибоначи на рекурсии с оптимизацией
# оптимизация заключается в сохранении полученных результатов, чтобы не вычислять по несколько раз
def fib_recur(k, calculated=None):
	if calculated is None:
		calculated=[1, 1]
	if k > len(calculated)-1:
		res = fib_recur(k-2, calculated) + fib_recur(k-1, calculated)
		calculated.append(res)
	return calculated[k]

# Числа Фибоначи на цикле
def fib_loop(k):
	a = 1; b = 1
	for i in range(1, k):
		a, b = b, a + b
	return b

def fib_loop_with_arr(k):
	calculated = [1, 1]
	for i in range(2, k+1):
		calculated.append(calculated[i-2] + calculated[i-1])
	return calculated[k]

def fib_loop_with_dict(k):
	calculated = {0: 1, 1: 1}
	for i in range(2, k+1):
		calculated[i] = calculated[i-2] + calculated[i-1]
	return calculated[k]

# for n in range(1, 200):
	# counter_recur = [0] * (n+1)
	# print(fib_recur_with_counter(n))
	# print(fib_recur(n))
	# print(fib_loop(n))
	# print(fib_loop_with_arr(n))
	# fib_loop_with_dict(n)

n = 10
print(timeit.timeit("fib_recur(n)", setup="from __main__ import fib_recur, n", number = 100000))
print(timeit.timeit("fib_loop(n)", setup="from __main__ import fib_loop, n", number = 100000))
print(timeit.timeit("fib_loop_with_arr(n)", setup="from __main__ import fib_loop_with_arr, n", number = 100000))
print(timeit.timeit("fib_loop_with_dict(n)", setup="from __main__ import fib_loop_with_dict, n", number = 100000))

'''
Вывод - рекурсия с пополнением массива
вышла стабильно быстрее более, чем в 10 раз,
по сравнению с перекладыванием переменных
'''