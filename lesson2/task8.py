number = int(input("Введите число: "))
example = int(input("Какую цифру считать?: "))
counter = 0

temp = number
while temp != 0:
	if temp % 10 == example:
		counter += 1
	temp = temp // 10

print(f"В числе {number} {counter} цифры {example}")