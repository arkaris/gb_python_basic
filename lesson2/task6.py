import random as rnd

print("Угадайте число от 1 до 100")
secret = rnd.randint(1,100)

success = False
counter = 10
while counter > 0:
	my_try = int(input("Ваш вариант: "))

	if my_try == secret:
		success = True
		break
	else:
		if secret < my_try:
			print("Загаданное число меньше")
		else:
			print("Загаданное число больше")
		counter -= 1
		print(f"Осталось {counter} попыток.")

if success:
	print("Вы угадали")
else:
	print(f"Попытки закончились. Было загадано число {secret}")