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

	if is_even(number % 10):
		even += 1
	else:
		odd += 1

	return even, odd

def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

main()