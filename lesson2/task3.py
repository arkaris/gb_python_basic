def main():
	number = int( input("Введите натуральное число: ") )
	print(reverse_number(number))

def reverse_number(number):
	if number < 10:
		return number
	else:
		right_symbol = number % 10
		return int( str(right_symbol) + str(reverse_number(number//10)) )

main()