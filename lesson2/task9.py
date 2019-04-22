# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def my_sum(number):
	if number < 10:
		return number
	else:
		return number % 10 + my_sum(number // 10)

def is_higher(num1, num2):
	return my_sum(num1) > my_sum(num2)

max_number = 0
while True:
	new_number = int(input("Введите натуральное число: "))
	if is_higher(new_number, max_number):
		max_number = new_number
	answer = input("Ввести еще одно число? (y/n): ")
	if answer != "y":
		break

print(f"Самая большая сумма цифр у числа {max_number} и равна {my_sum(max_number)}")