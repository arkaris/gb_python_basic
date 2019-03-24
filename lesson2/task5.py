row_counter = 0
row = ""
for i in range(32, 128):
	if row_counter != 0:
		row += "\t"

	row += str(i) + ":" + chr(i)

	row_counter = (row_counter + 1) % 10
	if row_counter == 0:
		print(row)
		row = ""