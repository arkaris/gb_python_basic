ROW_COUNT = 2
COLUMN_COUNT = 2

def request_item(matrix, i, j):
	return float(input(f"Введите значение {i} строки {j} столбца: "))

def append_row_sum(matrix):
	for row in matrix:
		row.append(sum(row))

def print_matrix(matrix):
	print("-"*(5*len(matrix[0])+3))
	for row in matrix:
		print("|", end="")
		for cell in row:
			print(f"{cell:>5}", end="")
		print(" |")
	print("-"*(5*len(matrix[0])+3))

matrix = []
for i in range(ROW_COUNT):
	matrix.append([])
	for j in range(COLUMN_COUNT):
		matrix[i].append(request_item(matrix, i, j))

append_row_sum(matrix)
print_matrix(matrix)