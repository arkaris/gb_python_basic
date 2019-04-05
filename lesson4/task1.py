import timeit
import math

# Числа Фибоначи на неоптимизированной рекурсии со счетчиком вызовов
def fib_recur_with_counter(k):
	counter_recur[k] += 1
	if k < 1: 
		return k + 1
	else:
		return fib_recur_with_counter(k - 1) + fib_recur_with_counter(k - 2)

# for n in range(1, 20):
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
def fib_recur(k, calculated=[1, 1]):
	if k > len(calculated)-1:
		res = fib_recur(k-2, calculated) + fib_recur(k-1, calculated)
		calculated.append(res)
	return calculated[k]

# Числа Фибоначи на цикле
def fib_loop(k):
	a = 1; b = 1
	if k > 1:
		for i in range(1, k):
			a, b = b, a + b
	return b

# for n in range(1, 10):
# 	counter_recur = [0] * (n+1)
# 	print(fib_recur_with_counter(n))
# 	print(fib_recur(n))
# 	print(fib_loop(n))

n = 50
print(timeit.timeit("fib_recur(n)", setup="from __main__ import fib_recur, n", number = 100000))
print(timeit.timeit("fib_loop(n)", setup="from __main__ import fib_loop, n", number = 100000))

'''
Вывод - рекурсия с пополнением массива
вышла стабильно быстрее более, чем в 10 раз,
по сравнению с перекладыванием переменных
'''