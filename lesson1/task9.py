a, b, c = map(float, input("Введите через один пробел три числа: ").split(" "))

if a == b or b == c or a == c:
	print("Числа совпадают")
	exit()

l = sorted([a, b, c])

print("{1} находится между {0} и {2}".format(*l))