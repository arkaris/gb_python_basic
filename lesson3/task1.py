for i in range(2, 10):
	counter = 0
	for j in range(2, 100):
		if j % i == 0:
			counter += 1
	print(f"Чисел, кратных {i}: {counter}")