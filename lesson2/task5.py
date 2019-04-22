# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

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