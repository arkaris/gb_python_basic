# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def main():
	number = int( input("Введите натуральное число:") )
	even, odd = calc_even(number)
	print("Четных цифр: ",even)
	print("Нечетных цифр: ",odd)

def calc_even(number):
	if number > 9:
		even, odd = calc_even(number//10)
	else:
		even, odd = 0, 0

	if is_even(number%10):
		even += 1
	else:
		odd += 1

	return even, odd

def is_even(number):
	return number % 2 == 0

main()