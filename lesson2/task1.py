def main():
	while True:
		variables = get_variables()
		result = calculate(*variables)
		print_result(result)
		if not ask_continue():
			break

def ask_continue():
	return input("Повторить? (y/n): ") == "y"

def get_variables():
	# operator
	operator = ""
	while operator not in ("+","-","*","/"):
		operator = input("Введите оператор: ")
	# value1
	value1 = float(input("Введите первый операнд: "))
	# value2
	while True:
		value2 = float(input("Введите второй операнд: "))
		if operator = "/" and value2 = 0:
			print("Деление на 0 запрещено")
		else:
			break
	# return
	return (operator, value1, value2)

def calculate(operator, value1, value2):
	if operator == "+":
		result = value1 + value2
	elif operator == "-":
		result = value1 - value2
	elif operator == "*":
		result = value1 * value2
	elif operator == "/":
		result = value1 / value2
	return result

def print_result(result):
	print(result)

main()