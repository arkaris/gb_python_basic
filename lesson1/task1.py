# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_input = input('Введите 3-значное число: ')
numbers = map(int, user_input)

numbers_sum = 0;
for number in numbers:
	numbers_sum += number
print("Сумма цифр:", numbers_sum)

numbers_mul = 1;
for number in numbers:
	numbers_mul *= number
print("Произведение цифр:", numbers_mul)

input('Работа завершена.')