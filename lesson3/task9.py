from random import randint
matrix = [[randint(-5, 5) for j in range(4)] for i in range(4)]

def print_matrix(matrix):
	for row in matrix:
		for cell in row:
			print(f"{cell:>5}", end="")
		print("")

print("Исходная матрица")
print_matrix(matrix)

result = max([min(row) for row in matrix])
print("Максимальное из минимальных по столбцам", result)