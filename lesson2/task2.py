# Считаем, что ноль не входит в перечень натуральных чисел
def main():
	number = int( input("Введите натуральное число:") )
	even, odd = calc_even(number)
	print("Четных цифр: ",even)
	print("Нечетных цифр: ",odd)

def calc_even(number):
	if number == 0:
		return (0, 0)
	else:
		even, odd = calc_even(number//10)
		symbol = number % 10
		if symbol % 2 == 0:
			even += 1
		else:
			odd += 1
		return (even, odd)

main()